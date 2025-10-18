# Ollama Test con Python

Questo progetto contiene esempi per interagire con Ollama usando Python e il modello Granite4.

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

### 1. `setup_check.py` - Verifica configurazione

Verifica che tutto sia configurato correttamente:

```bash
python setup_check.py
```

### 2. `ollama_basic.py` - Esempi base

Contiene funzioni per:
- Testare la connessione
- Chat semplice
- Generazione di testo
- Streaming delle risposte

```bash
python ollama_basic.py
```

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
├── readme.md              # Questa guida
├── ollama_basic.py         # Esempi base
├── ollama_advanced.py      # Client avanzato
├── ollama_http.py          # API HTTP dirette
├── chatbot.py             # Chatbot interattivo
└── .venv/                 # Ambiente virtuale Python
```

## Risorse utili

- [Documentazione Ollama](https://ollama.ai/docs)
- [API Reference](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Libreria Python ufficiale](https://pypi.org/project/ollama/)