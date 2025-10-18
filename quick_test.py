#!/usr/bin/env python3
"""
Test rapido per verificare connessione Ollama
"""

import ollama

# Test veloce
try:
    models = ollama.list()
    print(f"✅ Connesso! Modelli disponibili: {len(models.models)}")
    
    # Test generazione
    response = ollama.generate(model="granite4", prompt="Dimmi 'OK' se funziono")
    print(f"🤖 Risposta: {response['response'].strip()}")
    
except Exception as e:
    print(f"❌ Errore: {e}")
    print("Assicurati che Ollama sia in esecuzione: ollama serve")