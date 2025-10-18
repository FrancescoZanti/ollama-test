#!/usr/bin/env python3
"""
Esempio di utilizzo programmatico del sistema RAG

Questo script mostra come utilizzare il sistema RAG all'interno 
del proprio codice Python per creare applicazioni personalizzate.
"""

from rag_example import RAGSystem

def esempio_base():
    """Esempio base di utilizzo del sistema RAG"""
    print("=" * 70)
    print("📝 ESEMPIO 1: Utilizzo base del sistema RAG")
    print("=" * 70)
    
    # Inizializza il sistema
    rag = RAGSystem(pdf_folder="example/pdf", model_name="granite4")
    
    # Carica i documenti PDF
    documents = rag.load_pdfs()
    print(f"\n📚 Documenti caricati: {len(documents)}")
    
    # Crea gli embeddings (necessario solo una volta)
    rag.create_embeddings()
    
    # Fai una domanda
    domanda = "Che cos'è il machine learning?"
    risposta = rag.query(domanda, n_results=3, verbose=True)
    
    return rag

def esempio_multiple_query(rag_system):
    """Esempio di multiple query sullo stesso sistema"""
    print("\n" + "=" * 70)
    print("📝 ESEMPIO 2: Query multiple sullo stesso sistema")
    print("=" * 70)
    
    domande = [
        "Quali sono le principali applicazioni dell'intelligenza artificiale?",
        "Cosa si intende per sostenibilità ambientale?",
        "Quali sono state le principali missioni spaziali?",
    ]
    
    for i, domanda in enumerate(domande, 1):
        print(f"\n--- Domanda {i} ---")
        rag_system.query(domanda, n_results=2, verbose=True)

def esempio_ricerca_personalizzata(rag_system):
    """Esempio di ricerca personalizzata con accesso ai risultati"""
    print("\n" + "=" * 70)
    print("📝 ESEMPIO 3: Ricerca personalizzata")
    print("=" * 70)
    
    domanda = "neuroscienze"
    print(f"\n🔍 Ricerca di: '{domanda}'")
    
    # Esegui solo la ricerca senza generare risposta
    results = rag_system.search(domanda, n_results=5)
    
    if results and results.get('documents'):
        print(f"\n📄 Trovati {len(results['documents'][0])} risultati:")
        for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
            print(f"\n{i}. Fonte: {metadata['filename']}")
            print(f"   Anteprima: {doc[:200]}...")

def esempio_generazione_custom(rag_system):
    """Esempio di generazione con prompt personalizzato"""
    print("\n" + "=" * 70)
    print("📝 ESEMPIO 4: Generazione con prompt personalizzato")
    print("=" * 70)
    
    domanda = "intelligenza artificiale"
    
    # Cerca il contesto
    results = rag_system.search(domanda, n_results=2)
    
    if results and results.get('documents'):
        # Crea un contesto personalizzato
        context = "\n".join(results['documents'][0])
        
        # Crea un prompt personalizzato
        custom_prompt = f"""Basandoti sul seguente contesto, crea un riassunto 
in 3 punti chiave sull'intelligenza artificiale.

CONTESTO:
{context}

RIASSUNTO (3 punti):"""
        
        print("\n🤖 Generazione risposta con prompt personalizzato...")
        risposta = rag_system.generate_answer("", custom_prompt)
        print(f"\n💡 Risposta:\n{risposta}")

def esempio_statistiche(rag_system):
    """Mostra statistiche sui documenti caricati"""
    print("\n" + "=" * 70)
    print("📝 ESEMPIO 5: Statistiche sui documenti")
    print("=" * 70)
    
    print(f"\n📊 Statistiche:")
    print(f"   Documenti totali: {len(rag_system.documents)}")
    
    total_pages = sum(doc['pages'] for doc in rag_system.documents)
    total_chars = sum(len(doc['text']) for doc in rag_system.documents)
    
    print(f"   Pagine totali: {total_pages}")
    print(f"   Caratteri totali: {total_chars:,}")
    print(f"   Media caratteri per documento: {total_chars // len(rag_system.documents):,}")
    
    print(f"\n📚 Documenti:")
    for doc in rag_system.documents:
        print(f"   • {doc['filename']}")
        print(f"     Pagine: {doc['pages']}, Caratteri: {len(doc['text']):,}")

if __name__ == "__main__":
    print("\n🚀 Esempi di utilizzo del sistema RAG\n")
    
    # Esegui esempio base (inizializza il sistema)
    rag = esempio_base()
    
    # Esegui altri esempi usando lo stesso sistema
    esempio_multiple_query(rag)
    esempio_ricerca_personalizzata(rag)
    esempio_generazione_custom(rag)
    esempio_statistiche(rag)
    
    print("\n" + "=" * 70)
    print("✅ Tutti gli esempi completati!")
    print("=" * 70)
    print("\n💡 Suggerimento: Modifica questi esempi per creare la tua applicazione RAG!")
