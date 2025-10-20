#!/usr/bin/env python3
"""
Esempio base per interagire con Ollama usando la libreria ufficiale
"""

import config  # Carica configurazione da .env
import ollama

def test_connection():
    """Testa la connessione con Ollama"""
    try:
        # Lista i modelli disponibili
        models = ollama.list()
        print("Modelli disponibili:")
        for model in models.models:
            print(f"- {model.model}")
        return True
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return False

def chat_simple(prompt, model_name="granite4"):
    """Esempio di chat semplice"""
    try:
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']
    except Exception as e:
        print(f"Errore durante la chat: {e}")
        return None

def generate_simple(prompt, model_name="granite4"):
    """Esempio di generazione semplice"""
    try:
        response = ollama.generate(model=model_name, prompt=prompt)
        return response['response']
    except Exception as e:
        print(f"Errore durante la generazione: {e}")
        return None

def stream_chat(prompt, model_name="granite4"):
    """Esempio di chat con streaming"""
    try:
        stream = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': prompt}],
            stream=True,
        )
        
        print("Risposta in streaming:")
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        print()  # Nuova riga alla fine
    except Exception as e:
        print(f"Errore durante lo streaming: {e}")

if __name__ == "__main__":
    print("=== Test connessione Ollama ===")
    if test_connection():
        print("\n=== Chat semplice ===")
        risposta = chat_simple("Ciao! Puoi presentarti brevemente?")
        if risposta:
            print(f"Risposta: {risposta}")
        
        print("\n=== Generazione semplice ===")
        risposta = generate_simple("Scrivi una breve poesia sull'intelligenza artificiale")
        if risposta:
            print(f"Risposta: {risposta}")
        
        print("\n=== Chat con streaming ===")
        stream_chat("Spiegami in 3 punti cos'è il machine learning")