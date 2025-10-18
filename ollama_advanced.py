#!/usr/bin/env python3
"""
Esempi avanzati per interagire con Ollama
"""

import ollama
import json
from typing import List, Dict, Any

class OllamaClient:
    def __init__(self, model_name="granite4", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self.conversation_history = []
    
    def add_system_prompt(self, system_message: str):
        """Aggiunge un messaggio di sistema per definire il comportamento del modello"""
        self.conversation_history.insert(0, {
            'role': 'system',
            'content': system_message
        })
    
    def chat(self, message: str, save_to_history: bool = True) -> str:
        """Chat con mantenimento della cronologia"""
        # Aggiungi il messaggio dell'utente
        current_messages = self.conversation_history + [{
            'role': 'user',
            'content': message
        }]
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=current_messages
            )
            
            assistant_response = response['message']['content']
            
            if save_to_history:
                self.conversation_history.append({
                    'role': 'user',
                    'content': message
                })
                self.conversation_history.append({
                    'role': 'assistant',
                    'content': assistant_response
                })
            
            return assistant_response
            
        except Exception as e:
            return f"Errore: {e}"
    
    def clear_history(self):
        """Pulisce la cronologia della conversazione"""
        # Mantieni solo i messaggi di sistema
        self.conversation_history = [
            msg for msg in self.conversation_history 
            if msg['role'] == 'system'
        ]
    
    def get_history(self) -> List[Dict[str, str]]:
        """Restituisce la cronologia della conversazione"""
        return self.conversation_history
    
    def save_conversation(self, filename: str):
        """Salva la conversazione in un file JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
    
    def load_conversation(self, filename: str):
        """Carica una conversazione da un file JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.conversation_history = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} non trovato")
        except json.JSONDecodeError:
            print(f"Errore nel parsing del file {filename}")

def analyze_code(code: str, model_name="granite4") -> str:
    """Analizza del codice con Ollama"""
    prompt = f"""
Analizza il seguente codice e fornisci:
1. Una spiegazione di cosa fa
2. Eventuali problemi o miglioramenti
3. Suggerimenti per l'ottimizzazione

Codice:
```
{code}
```
"""
    
    try:
        response = ollama.generate(model=model_name, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nell'analisi: {e}"

def translate_text(text: str, target_language: str, model_name="granite4") -> str:
    """Traduce del testo usando Ollama"""
    prompt = f"Traduci il seguente testo in {target_language}:\n\n{text}"
    
    try:
        response = ollama.generate(model=model_name, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nella traduzione: {e}"

def summarize_text(text: str, max_sentences: int = 3, model_name="granite4") -> str:
    """Riassume un testo"""
    prompt = f"""
Riassumi il seguente testo in massimo {max_sentences} frasi:

{text}
"""
    
    try:
        response = ollama.generate(model=model_name, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Errore nel riassunto: {e}"

if __name__ == "__main__":
    # Esempio di utilizzo del client avanzato
    client = OllamaClient()
    
    # Aggiungi un prompt di sistema
    client.add_system_prompt(
        "Sei un assistente AI esperto in programmazione Python. "
        "Rispondi sempre in italiano e sii preciso e utile."
    )
    
    print("=== Chat con cronologia ===")
    print("Client:", client.chat("Ciao! Come ti chiami?"))
    print("Client:", client.chat("Puoi aiutarmi con Python?"))
    print("Client:", client.chat("Qual è stato il mio primo messaggio?"))
    
    # Salva la conversazione
    client.save_conversation("conversazione.json")
    print("\nConversazione salvata in 'conversazione.json'")
    
    print("\n=== Analisi codice ===")
    esempio_codice = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
    
    analisi = analyze_code(esempio_codice)
    print(f"Analisi: {analisi}")
    
    print("\n=== Traduzione ===")
    traduzione = translate_text("Hello, how are you today?", "italiano")
    print(f"Traduzione: {traduzione}")