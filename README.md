# 🤖 Ollama Test con Python

Questo progetto contiene esempi pratici e completi per interagire con Ollama usando Python e il modello Granite4.

```
   ╔═══════════════════════════════════════════════════════╗
   ║  🐍 Python + 🤖 Ollama + 💎 Granite4 = 🚀 AI Locale  ║
   ╚═══════════════════════════════════════════════════════╝
```

**Caratteristiche principali:**
- ✅ Esempi pratici e pronti all'uso
- 🔄 Supporto per streaming delle risposte
- 💬 Chatbot interattivo con cronologia
- 🛠️ Strumenti per programmatori (code review, refactoring)
- 📚 Documentazione completa con esempi di output
- 🎯 Script progressivi: da principiante ad avanzato

## 📑 Indice

- [Quick Start](#-quick-start)
- [Prerequisiti](#prerequisiti)
- [Installazione](#installazione)
- [Verifica Ollama](#verifica-ollama)
- [Script disponibili](#script-disponibili)
- [Diagrammi e Architettura](#-diagrammi-e-architettura)
- [Esempi di utilizzo](#esempi-di-utilizzo)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Struttura del progetto](#struttura-del-progetto)
- [Screenshot e Esempi](#-screenshot-e-esempi)
- [Risorse utili](#risorse-utili)

## 🚀 Quick Start

**Vuoi iniziare subito?** Segui questi 4 passi:

```bash
# 1️⃣ Clona il repository
git clone https://github.com/FrancescoZanti/ollama-test.git
cd ollama-test

# 2️⃣ Installa le dipendenze Python
pip install -r requirements.txt

# 3️⃣ Verifica che Ollama sia attivo (in un altro terminale)
ollama serve

# 4️⃣ Esegui il test rapido
python quick_test.py
```

**Risultato atteso:**
```
✅ Connesso! Modelli disponibili: 2
🤖 Risposta: OK
```

## Prerequisiti

- Ollama installato e in esecuzione sulla porta 11434
- Modello Granite4 scaricato
- Python 3.7+

## Installazione

1. Clona il repository
2. Crea un ambiente virtuale:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # oppure
   .venv\Scripts\activate     # Windows
   ```
3. Installa le dipendenze:
   ```bash
   pip install ollama requests
   ```

## Verifica Ollama

Prima di usare gli script, assicurati che Ollama sia in esecuzione:

```bash
# Verifica che Ollama sia attivo
curl http://localhost:11434/api/tags

# Oppure lista i modelli
ollama list
```

## Script disponibili

**📋 Non sai quale script usare?** [Vedi il confronto dettagliato](screenshots/script_comparison.txt)

### 1. `setup_check.py` - Verifica configurazione

Verifica che tutto sia configurato correttamente:

```bash
python setup_check.py
```

**Output di esempio:**
```
🔧 Verifica configurazione Ollama + Python
==================================================

📋 Versione Python:
🐍 Python versione: 3.11.0
✅ Versione Python compatibile

📋 Server Ollama:
✅ Server Ollama raggiungibile - 2 modelli disponibili
   📦 granite4:latest (3842.5 MB)
   📦 llama2:7b (3825.8 MB)

📋 Modelli Granite:
✅ Modelli Granite trovati: 1
   🔥 granite4:latest

🎉 Tutto configurato correttamente!
```

[Vedi output completo](screenshots/setup_check_output.txt)

### 2. `ollama_basic.py` - Esempi base

Contiene funzioni per:
- Testare la connessione
- Chat semplice
- Generazione di testo
- Streaming delle risposte

```bash
python ollama_basic.py
```

**Output di esempio:**
```
=== Test connessione Ollama ===
Modelli disponibili:
- granite4:latest
- llama2:7b

=== Chat semplice ===
Risposta: Ciao! Sono un assistente AI creato per aiutarti...

=== Chat con streaming ===
Risposta in streaming:
Ecco 3 punti chiave sul machine learning:
1. **Apprendimento dai dati**: ...
2. **Modelli predittivi**: ...
3. **Miglioramento continuo**: ...
```

[Vedi output completo](screenshots/ollama_basic_output.txt)

### 3. `ollama_advanced.py` - Esempi avanzati

Include una classe `OllamaClient` con:
- Gestione della cronologia delle conversazioni
- Prompt di sistema personalizzabili
- Salvataggio/caricamento conversazioni
- Funzioni per analisi codice e traduzione

```bash
python ollama_advanced.py
```

### 4. `ollama_http.py` - API HTTP dirette

Client che usa richieste HTTP dirette per:
- Maggior controllo sulle richieste
- Gestione personalizzata degli errori
- Streaming avanzato

```bash
python ollama_http.py
```

### 5. `chatbot.py` - Chatbot interattivo

Un chatbot completo con:
- Chat interattiva da terminale
- Comandi speciali (/help, /stats, /save, /quit)
- Salvataggio automatico delle conversazioni

```bash
python chatbot.py
```

**Esempio di sessione:**
```
🤖 Chatbot Ollama - Digita /help per i comandi disponibili

Tu: Ciao! Come funziona Python?

🤖: Ciao! Python è un linguaggio di programmazione interpretato...

Tu: /stats

📊 Statistiche conversazione:
- Messaggi totali: 4
- Messaggi utente: 2
- Messaggi assistente: 2
```

[Vedi sessione completa](screenshots/chatbot_session.txt)

### 6. `programming_tools.py` - Strumenti per programmatori

Strumenti specializzati per sviluppatori:
- Revisione automatica del codice
- Generazione documentazione
- Spiegazione errori
- Refactoring assistito
- Analisi performance

```bash
python programming_tools.py
```

**Esempio di revisione codice:**
```
🛠️ Strumenti di Programmazione con Ollama

Seleziona un'opzione:
1. Revisione codice

Inserisci il codice da revisionare:
>>> def calcola(x,y):
...     return x+y*2

📝 RISULTATI DELLA REVISIONE:

✅ Punti forti:
- Funzione semplice e compatta

⚠️ Suggerimenti:
1. Aggiungi spazi intorno agli operatori
2. Manca la documentazione (docstring)
3. I nomi dei parametri potrebbero essere più descrittivi
```

[Vedi output completo](screenshots/programming_tools_output.txt)

### 7. `rag_example.py` - Sistema RAG (Retrieval Augmented Generation)

Sistema RAG completo che utilizza i PDF in `example/pdf` per creare una knowledge base interrogabile:
- Caricamento automatico di PDF
- Estrazione e chunking intelligente del testo
- Creazione di embeddings con Ollama
- Database vettoriale con ChromaDB
- Ricerca semantica nel contenuto
- Generazione di risposte basate sul contesto recuperato

```bash
# Modalità interattiva
python rag_example.py

# Esegui query di esempio
python rag_example.py --demo

# Mostra aiuto
python rag_example.py --help
```

**Esempio di utilizzo interattivo:**
```
🤖 Sistema RAG (Retrieval Augmented Generation) con Ollama
======================================================================
📚 Caricamento PDF da example/pdf...
   Elaborazione: 01_intelligenza_artificiale_machine_learning.pdf
   ✅ 01_intelligenza_artificiale_machine_learning.pdf: 57 pagine estratte
   ...

✅ Caricati 5 documenti

🔄 Creazione embeddings e memorizzazione in ChromaDB...
   Processamento: 01_intelligenza_artificiale_machine_learning.pdf
   ✅ 01_intelligenza_artificiale_machine_learning.pdf: 325 chunks processati
   ...

✅ Database vettoriale creato con 1444 chunks

======================================================================
✅ Sistema RAG pronto!
======================================================================

Puoi fare domande sui seguenti documenti:
  • 01_intelligenza_artificiale_machine_learning.pdf
  • 02_cambiamento_climatico_sostenibilita.pdf
  • 03_storia_esplorazione_spaziale.pdf
  • 04_tecnologie_web_moderne.pdf
  • 05_neuroscienze_ricerca_cervello.pdf

Comandi speciali:
  /quit o /exit - Esci dal programma
  /docs - Mostra la lista dei documenti

======================================================================

❓ Fai una domanda: Cos'è l'intelligenza artificiale?

🔍 Ricerca nei documenti...

📄 Chunk rilevanti trovati:
   1. 01_intelligenza_artificiale_machine_learning.pdf (chunk 45)
   2. 01_intelligenza_artificiale_machine_learning.pdf (chunk 12)
   3. 01_intelligenza_artificiale_machine_learning.pdf (chunk 89)

🤖 Generazione risposta...

💡 Risposta:
L'intelligenza artificiale (IA) è una branca dell'informatica che si occupa
di creare sistemi in grado di eseguire compiti che normalmente richiederebbero
l'intelligenza umana...
```

**Caratteristiche del sistema RAG:**
- 📄 **Caricamento PDF**: Estrae testo da tutti i PDF nella cartella specificata
- ✂️ **Chunking intelligente**: Divide il testo in chunk con sovrapposizione per preservare il contesto
- 🧮 **Embeddings**: Utilizza Ollama per generare embeddings vettoriali
- 🗄️ **ChromaDB**: Memorizza e indicizza i chunk per una ricerca veloce
- 🔍 **Ricerca semantica**: Trova i chunk più rilevanti basandosi sul significato
- 🤖 **Generazione contestuale**: Produce risposte accurate basate solo sul contenuto recuperato
- 💬 **Modalità interattiva**: Permette di fare domande in modo conversazionale

**Utilizzo programmatico:**

Il file `example_rag_usage.py` contiene esempi pratici di come utilizzare il sistema RAG nel proprio codice:

```python
from rag_example import RAGSystem

# Inizializza e carica documenti
rag = RAGSystem(pdf_folder="example/pdf", model_name="granite4")
rag.load_pdfs()
rag.create_embeddings()

# Fai una domanda
risposta = rag.query("Cos'è l'intelligenza artificiale?")
print(risposta)

# Ricerca personalizzata
results = rag.search("machine learning", n_results=5)
for doc in results['documents'][0]:
    print(doc)
```

Esegui gli esempi con:
```bash
python example_rag_usage.py
```

## 📊 Diagrammi e Architettura

### Architettura del Sistema

Il progetto utilizza una architettura client-server dove gli script Python comunicano con il server Ollama locale:

```
┌─────────────────────────────────────────────────────────────┐
│                    UTENTE / SVILUPPATORE                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ Esegue script Python
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼─────────┐      ┌────────▼────────┐
│  Script Python  │      │   Chatbot CLI    │
│  (esempio)      │      │   (interattivo)  │
└────────┬────────┘      └────────┬─────────┘
         │                        │
         │  API Calls             │
         └────────┬───────────────┘
                  │
         ┌────────▼─────────┐
         │ Libreria ollama  │
         │  (Python SDK)    │
         └────────┬─────────┘
                  │
                  │ HTTP REST API (localhost:11434)
                  │
         ┌────────▼─────────┐
         │  Ollama Server   │
         └────────┬─────────┘
                  │
         ┌────────▼─────────┐
         │  Granite4 Model  │
         │   (~3.8 GB)      │
         └──────────────────┘
```

[Vedi architettura dettagliata](screenshots/architecture.txt)

### Workflow di Utilizzo

Flusso consigliato per iniziare:

```
1. Installa Ollama → 2. Avvia Server → 3. Scarica Granite4
                                              ↓
4. Setup Python   ← 5. Verifica Setup   ←   Pronto!
```

**Scelta dello Script:**
- 🚀 **Test veloce?** → `quick_test.py`
- 📚 **Imparare?** → `ollama_basic.py`
- 💻 **Sviluppare?** → `ollama_advanced.py`
- 💬 **Chat interattiva?** → `chatbot.py`
- 🔧 **Programmare?** → `programming_tools.py`
- 🌐 **HTTP API?** → `ollama_http.py`
- 🔍 **RAG con PDF?** → `rag_example.py`

[Vedi workflow dettagliato](screenshots/workflow.txt)

## Esempi di utilizzo

### Chat semplice
```python
import ollama

response = ollama.chat(model='granite4', messages=[
    {'role': 'user', 'content': 'Ciao! Come stai?'}
])
print(response['message']['content'])
```

### Generazione con streaming
```python
import ollama

stream = ollama.generate(
    model='granite4',
    prompt='Racconta una storia breve',
    stream=True
)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
```

### Chat con cronologia
```python
from ollama_advanced import OllamaClient

client = OllamaClient()
client.add_system_prompt("Sei un esperto di Python")

risposta1 = client.chat("Cos'è una lista in Python?")
risposta2 = client.chat("Puoi farmi un esempio?")  # Sa del contesto precedente
```

## API Endpoints

Ollama espone diverse API REST:

- `GET /api/tags` - Lista modelli
- `POST /api/generate` - Genera testo
- `POST /api/chat` - Chat con cronologia
- `POST /api/embeddings` - Genera embeddings

## Troubleshooting

### Errore di connessione
- Verifica che Ollama sia in esecuzione: `ollama serve`
- Controlla la porta: dovrebbe essere 11434
- Testa con curl: `curl http://localhost:11434/api/tags`

### Modello non trovato
- Lista i modelli disponibili: `ollama list`
- Scarica Granite4 se necessario: `ollama pull granite4`

### Errori di memoria
- Granite4 richiede RAM sufficiente
- Considera modelli più piccoli per test: `ollama pull llama2:7b`

## Struttura del progetto

```
ollama-test/
├── README.md                      # 📖 Questa guida completa
├── requirements.txt               # 📦 Dipendenze Python
├── .gitignore                     # 🚫 File da escludere da git
│
├── setup_check.py                 # 🔍 Verifica configurazione
├── quick_test.py                  # ⚡ Test rapido connessione
│
├── ollama_basic.py                # 📚 Esempi base per iniziare
├── ollama_advanced.py             # 🎓 Client avanzato con cronologia
├── ollama_http.py                 # 🌐 API HTTP dirette
│
├── chatbot.py                     # 💬 Chatbot interattivo
├── programming_tools.py           # 🛠️ Strumenti per sviluppatori
├── rag_example.py                 # 🔍 Sistema RAG con PDF
├── example_rag_usage.py           # 📖 Esempi di utilizzo RAG
│
├── example/                       # 📁 Esempi e risorse
│   └── pdf/                       # 📄 PDF per il sistema RAG
│       ├── 01_intelligenza_artificiale_machine_learning.pdf
│       ├── 02_cambiamento_climatico_sostenibilita.pdf
│       ├── 03_storia_esplorazione_spaziale.pdf
│       ├── 04_tecnologie_web_moderne.pdf
│       └── 05_neuroscienze_ricerca_cervello.pdf
│
├── screenshots/                   # 📸 Esempi di output e diagrammi
│   ├── architecture.txt           #     Architettura del sistema
│   ├── workflow.txt               #     Flusso di lavoro
│   ├── setup_check_output.txt     #     Output di esempio
│   ├── ollama_basic_output.txt    #     Esempi di esecuzione
│   ├── chatbot_session.txt        #     Sessione chat esempio
│   └── programming_tools_output.txt
│
└── .venv/                         # 🐍 Ambiente virtuale Python
```

## 📸 Screenshot e Esempi

Tutti gli esempi di output e i diagrammi sono disponibili nella cartella `screenshots/`:

- 📐 [Architettura del sistema](screenshots/architecture.txt) - Diagramma completo dell'architettura
- 🔄 [Workflow di utilizzo](screenshots/workflow.txt) - Guida passo-passo per ogni scenario
- 📊 [Confronto script](screenshots/script_comparison.txt) - Quale script usare e quando
- 💻 [Output setup_check.py](screenshots/setup_check_output.txt) - Esempio di verifica configurazione
- 🐍 [Output ollama_basic.py](screenshots/ollama_basic_output.txt) - Esempi base in esecuzione
- 💬 [Sessione chatbot.py](screenshots/chatbot_session.txt) - Esempio di conversazione
- 🛠️ [Output programming_tools.py](screenshots/programming_tools_output.txt) - Code review esempio

## Risorse utili

- [Documentazione Ollama](https://ollama.ai/docs)
- [API Reference](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Libreria Python ufficiale](https://pypi.org/project/ollama/)

---

**💡 Suggerimento**: Inizia con `python quick_test.py` per verificare che tutto funzioni, poi esplora gli altri script!