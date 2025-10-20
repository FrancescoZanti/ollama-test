#!/usr/bin/env python3
"""
Esempio di sistema RAG (Retrieval Augmented Generation) con Ollama
Utilizza i PDF nella cartella example/pdf per creare una knowledge base interrogabile
"""

import config  # Carica configurazione da .env
import ollama
import chromadb
from pypdf import PdfReader
from pathlib import Path
import sys
from typing import List, Dict, Any

class RAGSystem:
    def __init__(self, pdf_folder: str = "example/pdf", model_name: str = "granite4"):
        """
        Inizializza il sistema RAG
        
        Args:
            pdf_folder: Percorso della cartella contenente i PDF
            model_name: Nome del modello Ollama da utilizzare
        """
        self.pdf_folder = Path(pdf_folder)
        self.model_name = model_name
        self.client = chromadb.Client()
        self.collection = None
        self.documents = []
        
    def load_pdfs(self) -> List[Dict[str, Any]]:
        """Carica e estrae il testo da tutti i PDF nella cartella"""
        print(f"📚 Caricamento PDF da {self.pdf_folder}...")
        
        documents = []
        pdf_files = list(self.pdf_folder.glob("*.pdf"))
        
        if not pdf_files:
            print(f"⚠️  Nessun PDF trovato in {self.pdf_folder}")
            return documents
            
        for pdf_file in pdf_files:
            try:
                print(f"   Elaborazione: {pdf_file.name}")
                reader = PdfReader(pdf_file)
                
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                
                documents.append({
                    'filename': pdf_file.name,
                    'text': text,
                    'pages': len(reader.pages)
                })
                
                print(f"   ✅ {pdf_file.name}: {len(reader.pages)} pagine estratte")
            except Exception as e:
                print(f"   ❌ Errore durante il caricamento di {pdf_file.name}: {e}")
        
        self.documents = documents
        print(f"\n✅ Caricati {len(documents)} documenti")
        return documents
    
    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """
        Divide il testo in chunk sovrapposti per un miglior contesto
        
        Args:
            text: Testo da dividere
            chunk_size: Dimensione di ogni chunk in caratteri
            overlap: Sovrapposizione tra chunk consecutivi
        """
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            
            # Cerca di terminare su un punto o spazio per non spezzare le frasi
            if end < len(text):
                last_period = chunk.rfind('.')
                last_space = chunk.rfind(' ')
                break_point = max(last_period, last_space)
                
                if break_point > chunk_size // 2:
                    chunk = text[start:start + break_point + 1]
                    end = start + break_point + 1
            
            chunks.append(chunk.strip())
            start = end - overlap
        
        return chunks
    
    def create_embeddings(self):
        """Crea embeddings per i documenti e li memorizza in ChromaDB"""
        print("\n🔄 Creazione embeddings e memorizzazione in ChromaDB...")
        
        # Crea o ottieni la collezione
        try:
            self.client.delete_collection("pdf_knowledge")
        except:
            pass
        
        self.collection = self.client.create_collection(
            name="pdf_knowledge",
            metadata={"description": "Knowledge base da PDF"}
        )
        
        chunk_id = 0
        for doc in self.documents:
            print(f"   Processamento: {doc['filename']}")
            chunks = self.chunk_text(doc['text'])
            
            for chunk in chunks:
                # Genera embedding usando Ollama
                try:
                    embedding_response = ollama.embeddings(
                        model=self.model_name,
                        prompt=chunk
                    )
                    embedding = embedding_response['embedding']
                    
                    # Aggiungi alla collezione
                    self.collection.add(
                        ids=[f"chunk_{chunk_id}"],
                        embeddings=[embedding],
                        documents=[chunk],
                        metadatas=[{
                            "filename": doc['filename'],
                            "chunk_index": chunk_id
                        }]
                    )
                    chunk_id += 1
                except Exception as e:
                    print(f"   ⚠️  Errore durante l'embedding del chunk: {e}")
            
            print(f"   ✅ {doc['filename']}: {len(chunks)} chunks processati")
        
        print(f"\n✅ Database vettoriale creato con {chunk_id} chunks")
    
    def search(self, query: str, n_results: int = 3) -> List[Dict[str, Any]]:
        """
        Cerca i chunk più rilevanti per una query
        
        Args:
            query: Domanda dell'utente
            n_results: Numero di risultati da restituire
        """
        if not self.collection:
            print("❌ Database non inizializzato. Esegui prima create_embeddings()")
            return []
        
        try:
            # Genera embedding per la query
            query_embedding = ollama.embeddings(
                model=self.model_name,
                prompt=query
            )['embedding']
            
            # Cerca i chunk più simili
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            
            return results
        except Exception as e:
            print(f"❌ Errore durante la ricerca: {e}")
            return {}
    
    def generate_answer(self, query: str, context: str) -> str:
        """
        Genera una risposta usando il contesto recuperato
        
        Args:
            query: Domanda dell'utente
            context: Contesto recuperato dal database vettoriale
        """
        prompt = f"""Basandoti ESCLUSIVAMENTE sul seguente contesto, rispondi alla domanda dell'utente.
Se la risposta non è presente nel contesto, dillo chiaramente.

CONTESTO:
{context}

DOMANDA: {query}

RISPOSTA:"""
        
        try:
            response = ollama.generate(
                model=self.model_name,
                prompt=prompt
            )
            return response['response']
        except Exception as e:
            return f"❌ Errore durante la generazione della risposta: {e}"
    
    def query(self, question: str, n_results: int = 3, verbose: bool = True) -> str:
        """
        Esegue una query completa: ricerca + generazione risposta
        
        Args:
            question: Domanda dell'utente
            n_results: Numero di chunk da recuperare
            verbose: Se True, mostra informazioni aggiuntive
        """
        if verbose:
            print(f"\n❓ Domanda: {question}")
            print(f"🔍 Ricerca nei documenti...")
        
        # Cerca i chunk rilevanti
        results = self.search(question, n_results)
        
        if not results or not results.get('documents'):
            return "❌ Nessun risultato trovato nel database"
        
        # Prepara il contesto
        context_parts = []
        if verbose:
            print(f"\n📄 Chunk rilevanti trovati:")
        
        for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
            if verbose:
                print(f"   {i+1}. {metadata['filename']} (chunk {metadata['chunk_index']})")
            context_parts.append(f"[Fonte: {metadata['filename']}]\n{doc}")
        
        context = "\n\n---\n\n".join(context_parts)
        
        # Genera la risposta
        if verbose:
            print(f"\n🤖 Generazione risposta...")
        
        answer = self.generate_answer(question, context)
        
        if verbose:
            print(f"\n💡 Risposta:\n{answer}")
        
        return answer

def demo_interattiva():
    """Modalità interattiva per interrogare il sistema RAG"""
    print("=" * 70)
    print("🤖 Sistema RAG (Retrieval Augmented Generation) con Ollama")
    print("=" * 70)
    
    # Inizializza il sistema
    rag = RAGSystem()
    
    # Carica i PDF
    documents = rag.load_pdfs()
    
    if not documents:
        print("❌ Impossibile procedere senza documenti")
        return
    
    # Crea gli embeddings
    rag.create_embeddings()
    
    print("\n" + "=" * 70)
    print("✅ Sistema RAG pronto!")
    print("=" * 70)
    print("\nPuoi fare domande sui seguenti documenti:")
    for doc in documents:
        print(f"  • {doc['filename']}")
    
    print("\nComandi speciali:")
    print("  /quit o /exit - Esci dal programma")
    print("  /docs - Mostra la lista dei documenti")
    print("\n" + "=" * 70)
    
    # Loop interattivo
    while True:
        try:
            domanda = input("\n❓ Fai una domanda: ").strip()
            
            if not domanda:
                continue
            
            if domanda.lower() in ['/quit', '/exit']:
                print("\n👋 Arrivederci!")
                break
            
            if domanda.lower() == '/docs':
                print("\n📚 Documenti disponibili:")
                for doc in documents:
                    print(f"  • {doc['filename']} ({doc['pages']} pagine)")
                continue
            
            # Esegui la query
            rag.query(domanda)
            
        except KeyboardInterrupt:
            print("\n\n👋 Arrivederci!")
            break
        except Exception as e:
            print(f"\n❌ Errore: {e}")

def demo_esempi():
    """Esempi di query predefinite per mostrare le capacità del sistema"""
    print("=" * 70)
    print("🤖 Esempi di utilizzo del sistema RAG")
    print("=" * 70)
    
    # Inizializza il sistema
    rag = RAGSystem()
    
    # Carica i PDF
    documents = rag.load_pdfs()
    
    if not documents:
        print("❌ Impossibile procedere senza documenti")
        return
    
    # Crea gli embeddings
    rag.create_embeddings()
    
    print("\n" + "=" * 70)
    print("📝 Esecuzione query di esempio")
    print("=" * 70)
    
    # Esempi di domande
    domande_esempio = [
        "Cos'è l'intelligenza artificiale?",
        "Quali sono le principali tecnologie web moderne?",
        "Qual è l'impatto del cambiamento climatico?",
    ]
    
    for domanda in domande_esempio:
        rag.query(domanda)
        print("\n" + "-" * 70)

if __name__ == "__main__":
    print("\n🚀 Avvio sistema RAG con Ollama\n")
    
    # Controlla gli argomenti della riga di comando
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            demo_esempi()
        elif sys.argv[1] == "--help":
            print("Utilizzo:")
            print("  python rag_example.py           # Modalità interattiva")
            print("  python rag_example.py --demo    # Esegui query di esempio")
            print("  python rag_example.py --help    # Mostra questo messaggio")
        else:
            print(f"❌ Opzione non riconosciuta: {sys.argv[1]}")
            print("Usa --help per vedere le opzioni disponibili")
    else:
        # Modalità interattiva predefinita
        demo_interattiva()
