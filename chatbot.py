#!/usr/bin/env python3
"""
Esempio di chatbot interattivo con Ollama
"""

import ollama
import sys
from datetime import datetime
from config import get_ollama_base_url

class ChatBot:
    def __init__(self, model_name="granite4"):
        self.model_name = model_name
        self.conversation = []
        self.system_prompt = """Sei un assistente AI utile e amichevole. 
Rispondi sempre in italiano in modo chiaro e conciso. 
Se non conosci la risposta, dillo onestamente."""
        
        # Aggiungi il prompt di sistema
        self.conversation.append({
            'role': 'system',
            'content': self.system_prompt
        })
    
    def chat(self, user_input: str) -> str:
        """Invia un messaggio e ricevi una risposta"""
        # Aggiungi il messaggio dell'utente
        self.conversation.append({
            'role': 'user',
            'content': user_input
        })
        
        try:
            # Ottieni la risposta dal modello
            response = ollama.chat(
                model=self.model_name,
                messages=self.conversation
            )
            
            assistant_response = response['message']['content']
            
            # Aggiungi la risposta alla conversazione
            self.conversation.append({
                'role': 'assistant',
                'content': assistant_response
            })
            
            return assistant_response
            
        except Exception as e:
            error_msg = f"Errore nella comunicazione con Ollama: {e}"
            print(error_msg)
            return error_msg
    
    def save_conversation(self, filename: str = None):
        """Salva la conversazione corrente"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chat_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== Conversazione Ollama - {datetime.now()} ===\n\n")
            for msg in self.conversation:
                if msg['role'] != 'system':
                    role = "🤖 Assistente" if msg['role'] == 'assistant' else "👤 Utente"
                    f.write(f"{role}: {msg['content']}\n\n")
        
        print(f"Conversazione salvata in: {filename}")
    
    def get_stats(self):
        """Mostra statistiche della conversazione"""
        user_messages = len([msg for msg in self.conversation if msg['role'] == 'user'])
        assistant_messages = len([msg for msg in self.conversation if msg['role'] == 'assistant'])
        total_chars = sum(len(msg['content']) for msg in self.conversation if msg['role'] != 'system')
        
        return {
            'messaggi_utente': user_messages,
            'messaggi_assistente': assistant_messages,
            'caratteri_totali': total_chars
        }

def run_interactive_chat():
    """Avvia una chat interattiva"""
    print("🤖 Chatbot Ollama - Granite4")
    print("=" * 40)
    print("Comandi speciali:")
    print("  /help    - Mostra questo messaggio")
    print("  /stats   - Mostra statistiche")
    print("  /save    - Salva conversazione")
    print("  /clear   - Pulisci schermo")
    print("  /quit    - Esci")
    print("=" * 40)
    
    bot = ChatBot()
    
    # Test iniziale della connessione
    base_url = get_ollama_base_url()
    try:
        test_response = ollama.list()
        print(f"✅ Connesso a Ollama su {base_url}")
        print(f"   Modelli disponibili: {len(test_response['models'])}")
    except Exception as e:
        print(f"❌ Errore di connessione a Ollama su {base_url}: {e}")
        print("Assicurati che Ollama sia in esecuzione")
        return
    
    print("\n💬 Inizia a chattare! (scrivi /quit per uscire)\n")
    
    while True:
        try:
            user_input = input("👤 Tu: ").strip()
            
            if not user_input:
                continue
            
            # Gestisci comandi speciali
            if user_input.startswith('/'):
                command = user_input[1:].lower()
                
                if command == 'quit':
                    print("👋 Arrivederci!")
                    break
                elif command == 'help':
                    print("\nComandi disponibili:")
                    print("  /help    - Mostra questo messaggio")
                    print("  /stats   - Mostra statistiche")
                    print("  /save    - Salva conversazione")
                    print("  /clear   - Pulisci schermo")
                    print("  /quit    - Esci\n")
                    continue
                elif command == 'stats':
                    stats = bot.get_stats()
                    print(f"\n📊 Statistiche:")
                    print(f"   Tuoi messaggi: {stats['messaggi_utente']}")
                    print(f"   Risposte bot: {stats['messaggi_assistente']}")
                    print(f"   Caratteri totali: {stats['caratteri_totali']}\n")
                    continue
                elif command == 'save':
                    bot.save_conversation()
                    continue
                elif command == 'clear':
                    import os
                    os.system('clear' if os.name == 'posix' else 'cls')
                    continue
                else:
                    print(f"Comando sconosciuto: {command}")
                    continue
            
            # Invia il messaggio al bot
            print("🤖 Assistente: ", end="", flush=True)
            response = bot.chat(user_input)
            print(response)
            print()  # Riga vuota per separare
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrotta. Arrivederci!")
            break
        except Exception as e:
            print(f"\n❌ Errore imprevisto: {e}")
            print("Riprova o scrivi /quit per uscire\n")

if __name__ == "__main__":
    run_interactive_chat()