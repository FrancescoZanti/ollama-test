#!/usr/bin/env python3
"""
Esempi pratici di utilizzo di Ollama con Granite4
"""

import config  # Carica configurazione da .env
import ollama
import json
import time
from datetime import datetime

def code_reviewer(code: str, language: str = "python") -> str:
    """Revisione automatica del codice"""
    prompt = f"""
Revisiona questo codice {language} e fornisci:

1. ANALISI: Cosa fa il codice
2. PROBLEMI: Eventuali bug o problemi
3. MIGLIORAMENTI: Suggerimenti per ottimizzare
4. SICUREZZA: Considerazioni sulla sicurezza

Codice da revisionare:
```{language}
{code}
```

Rispondi in formato strutturato e in italiano.
"""
    
    try:
        response = ollama.generate(model="granite4", prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nella revisione: {e}"

def documentation_generator(function_code: str) -> str:
    """Genera documentazione per una funzione"""
    prompt = f"""
Genera documentazione completa per questa funzione Python:

{function_code}

Includi:
- Docstring dettagliata
- Parametri e tipi
- Valore di ritorno
- Esempi di utilizzo
- Possibili eccezioni

Rispondi solo con la documentazione formattata.
"""
    
    try:
        response = ollama.generate(model="granite4", prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nella generazione: {e}"

def explain_error(error_message: str, context: str = "") -> str:
    """Spiega un errore e suggerisce soluzioni"""
    prompt = f"""
Spiega questo errore Python e suggerisci come risolverlo:

ERRORE: {error_message}

CONTESTO: {context}

Fornisci:
1. Spiegazione dell'errore
2. Cause più comuni
3. Soluzioni step-by-step
4. Come prevenirlo in futuro

Rispondi in italiano in modo chiaro e pratico.
"""
    
    try:
        response = ollama.generate(model="granite4", prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nella spiegazione: {e}"

def refactor_code(code: str, goal: str) -> str:
    """Refactoring del codice secondo obiettivi specifici"""
    prompt = f"""
Refactorizza questo codice Python per: {goal}

Codice originale:
```python
{code}
```

Fornisci:
1. Codice refactorizzato
2. Spiegazione dei cambiamenti
3. Vantaggi della nuova versione

Mantieni la funzionalità originale.
"""
    
    try:
        response = ollama.generate(model="granite4", prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nel refactoring: {e}"

def performance_analyzer(code: str) -> str:
    """Analisi delle performance del codice"""
    prompt = f"""
Analizza le performance di questo codice Python:

```python
{code}
```

Valuta:
1. Complessità temporale (Big O)
2. Utilizzo memoria
3. Bottleneck principali
4. Ottimizzazioni possibili
5. Codice alternativo più efficiente

Sii specifico e tecnico.
"""
    
    try:
        response = ollama.generate(model="granite4", prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nell'analisi: {e}"

class ProgrammingAssistant:
    """Assistente programmazione con Ollama"""
    
    def __init__(self, model="granite4"):
        self.model = model
        self.session_history = []
    
    def ask_programming_question(self, question: str, code_context: str = "") -> str:
        """Fai una domanda di programmazione"""
        context_part = f"\n\nCONTESTO CODICE:\n```python\n{code_context}\n```" if code_context else ""
        
        prompt = f"""
Domanda di programmazione: {question}{context_part}

Rispondi come un senior developer Python. Sii pratico, fornisci esempi di codice quando utile, e spiega i concetti chiaramente.
"""
        
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Sei un senior Python developer esperto. Rispondi sempre in italiano con esempi pratici."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            answer = response['message']['content']
            
            # Salva nella cronologia
            self.session_history.append({
                "timestamp": datetime.now().isoformat(),
                "question": question,
                "answer": answer,
                "context": code_context
            })
            
            return answer
        except Exception as e:
            return f"Errore: {e}"
    
    def explain_concept(self, concept: str, level: str = "intermediate") -> str:
        """Spiega un concetto di programmazione"""
        prompt = f"""
Spiega il concetto: "{concept}"

Livello: {level} (beginner/intermediate/advanced)

Includi:
1. Definizione chiara
2. Quando e perché usarlo
3. Esempi pratici di codice
4. Best practices
5. Errori comuni da evitare

Usa un linguaggio appropriato al livello richiesto.
"""
        
        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"Errore: {e}"
    
    def save_session(self, filename: str = None):
        """Salva la sessione corrente"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"programming_session_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.session_history, f, ensure_ascii=False, indent=2)
        
        return filename

def interactive_demo():
    """Demo interattiva degli strumenti"""
    print("🚀 Demo Strumenti Programmazione con Ollama")
    print("=" * 50)
    
    # Esempio 1: Revisione codice
    print("\n1️⃣ REVISIONE CODICE")
    esempio_codice = '''
def calcola_fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * calcola_fattoriale(n-1)
'''
    
    print(f"Codice da revisionare:\n{esempio_codice}")
    print("Revisione in corso...")
    revisione = code_reviewer(esempio_codice)
    print(f"RISULTATO:\n{revisione}\n")
    
    # Esempio 2: Spiegazione errore
    print("2️⃣ SPIEGAZIONE ERRORE")
    errore = "IndexError: list index out of range"
    contesto = "Stavo accedendo a lista[5] ma la lista ha solo 3 elementi"
    
    print(f"Errore: {errore}")
    print(f"Contesto: {contesto}")
    print("Analisi in corso...")
    spiegazione = explain_error(errore, contesto)
    print(f"SPIEGAZIONE:\n{spiegazione}\n")
    
    # Esempio 3: Assistente programmazione
    print("3️⃣ ASSISTENTE PROGRAMMAZIONE")
    assistant = ProgrammingAssistant()
    
    domanda = "Come posso ottimizzare una funzione che cerca un elemento in una lista?"
    print(f"Domanda: {domanda}")
    print("Elaborazione risposta...")
    risposta = assistant.ask_programming_question(domanda)
    print(f"RISPOSTA:\n{risposta}\n")
    
    # Salva sessione
    filename = assistant.save_session()
    print(f"💾 Sessione salvata in: {filename}")

if __name__ == "__main__":
    interactive_demo()