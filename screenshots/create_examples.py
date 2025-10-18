#!/usr/bin/env python3
"""
Script per creare file di esempio che mostrano l'output dei vari script
"""

import os

# Crea esempi di output per ogni script
examples = {
    "setup_check_output.txt": """🔧 Verifica configurazione Ollama + Python
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

📋 Libreria Python:
✅ Libreria ollama importata correttamente
✅ API ollama funzionante - 2 modelli

📋 Test generazione:
🧪 Test generazione con granite4:latest...
✅ Test completato! Risposta: Ciao!

==================================================
📊 RISULTATI:
   ✅ PASS - Versione Python
   ✅ PASS - Server Ollama
   ✅ PASS - Modelli Granite
   ✅ PASS - Libreria Python
   ✅ PASS - Test generazione

🎉 Tutto configurato correttamente!
   Puoi iniziare a usare gli script di esempio.
""",

    "ollama_basic_output.txt": """=== Test connessione Ollama ===
Modelli disponibili:
- granite4:latest
- llama2:7b

=== Chat semplice ===
Risposta: Ciao! Sono un assistente AI creato per aiutarti. Posso 
rispondere a domande, fornire informazioni, aiutarti con la 
programmazione e molto altro. Come posso aiutarti oggi?

=== Generazione semplice ===
Risposta: Nel silenzio dei circuiti,
nasce un pensiero digitale,
un'eco di intelligenza
che danza tra i bit,
cercando di comprendere
l'essenza dell'umano.

=== Chat con streaming ===
Risposta in streaming:
Ecco 3 punti chiave sul machine learning:

1. **Apprendimento dai dati**: Il machine learning permette ai 
   computer di imparare automaticamente dai dati senza essere 
   esplicitamente programmati per ogni caso.

2. **Modelli predittivi**: Crea modelli che possono fare previsioni 
   o prendere decisioni basandosi su pattern identificati nei dati 
   di addestramento.

3. **Miglioramento continuo**: I modelli migliorano le loro 
   performance man mano che vengono esposti a più dati, adattandosi 
   a nuovi pattern e situazioni.
""",

    "chatbot_session.txt": """🤖 Chatbot Ollama - Digita /help per i comandi disponibili

Tu: Ciao! Come funziona Python?

🤖: Ciao! Python è un linguaggio di programmazione interpretato e di 
alto livello. Funziona attraverso:

1. L'interprete Python legge il codice riga per riga
2. Converte il codice in bytecode
3. Esegue il bytecode nella Python Virtual Machine (PVM)

È famoso per la sua sintassi chiara e leggibile che lo rende ideale 
per principianti e professionisti.

Tu: Puoi farmi un esempio di funzione?

🤖: Certamente! Ecco un esempio di funzione in Python:

```python
def saluta(nome):
    \"\"\"Funzione che saluta una persona\"\"\"
    messaggio = f"Ciao, {nome}! Benvenuto!"
    return messaggio

# Uso della funzione
risultato = saluta("Mario")
print(risultato)  # Output: Ciao, Mario! Benvenuto!
```

Questa funzione accetta un parametro 'nome' e restituisce un 
messaggio di saluto personalizzato.

Tu: /stats

📊 Statistiche conversazione:
- Messaggi totali: 4
- Messaggi utente: 2
- Messaggi assistente: 2
- Modello: granite4
- Durata sessione: 2 minuti

Tu: /quit

👋 Arrivederci! Conversazione salvata.
""",

    "programming_tools_output.txt": """🛠️ Strumenti di Programmazione con Ollama
==========================================

Seleziona un'opzione:
1. Revisione codice
2. Genera documentazione
3. Spiega errore
4. Refactoring assistito
5. Analisi performance

Scelta: 1

Inserisci il codice da revisionare:
>>> def calcola(x,y):
...     return x+y*2

🔍 Analisi del codice in corso...

📝 RISULTATI DELLA REVISIONE:

✅ Punti forti:
- Funzione semplice e compatta
- Nome descrittivo

⚠️ Suggerimenti:
1. Aggiungi spazi intorno agli operatori per migliorare leggibilità
2. Manca la documentazione (docstring)
3. I nomi dei parametri potrebbero essere più descrittivi
4. Considera di validare i tipi degli input

💡 Codice migliorato:
```python
def calcola(primo_numero, secondo_numero):
    \"\"\"
    Calcola il risultato di: primo_numero + (secondo_numero * 2)
    
    Args:
        primo_numero: Il primo numero dell'operazione
        secondo_numero: Il numero che verrà moltiplicato per 2
        
    Returns:
        Il risultato del calcolo
    \"\"\"
    return primo_numero + (secondo_numero * 2)
```

Vuoi salvare il codice migliorato? (s/n): s
✅ Codice salvato in 'calcola_improved.py'
"""
}

# Crea i file di esempio
screenshots_dir = "/home/runner/work/ollama-test/ollama-test/screenshots"
for filename, content in examples.items():
    filepath = os.path.join(screenshots_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Creato: {filename}")

print(f"\n🎉 Creati {len(examples)} file di esempio in {screenshots_dir}")
