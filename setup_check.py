#!/usr/bin/env python3
"""
Script di configurazione e test per verificare l'ambiente Ollama
"""

import sys
import subprocess
import requests
import json

def check_python_version():
    """Verifica la versione di Python"""
    version = sys.version_info
    print(f"🐍 Python versione: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ è richiesto")
        return False
    else:
        print("✅ Versione Python compatibile")
        return True

def check_ollama_server():
    """Verifica che il server Ollama sia raggiungibile"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json()
            print(f"✅ Server Ollama raggiungibile - {len(models['models'])} modelli disponibili")
            
            # Mostra i modelli
            for model in models['models']:
                size_mb = model['size'] / (1024 * 1024)
                print(f"   📦 {model['name']} ({size_mb:.1f} MB)")
            
            return True
        else:
            print(f"❌ Server Ollama risponde con codice: {response.status_code}")
            return False
    except requests.ConnectionError:
        print("❌ Impossibile connettersi al server Ollama")
        print("   Assicurati che Ollama sia in esecuzione:")
        print("   ollama serve")
        return False
    except requests.Timeout:
        print("❌ Timeout nella connessione al server Ollama")
        return False
    except Exception as e:
        print(f"❌ Errore nella verifica del server: {e}")
        return False

def check_granite4_model():
    """Verifica che il modello Granite4 sia disponibile"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json()
            granite_models = [m for m in models['models'] if 'granite' in m['name'].lower()]
            
            if granite_models:
                print(f"✅ Modelli Granite trovati: {len(granite_models)}")
                for model in granite_models:
                    print(f"   🔥 {model['name']}")
                return True
            else:
                print("❌ Nessun modello Granite trovato")
                print("   Per scaricare Granite4:")
                print("   ollama pull granite4")
                return False
    except Exception as e:
        print(f"❌ Errore nella verifica dei modelli: {e}")
        return False

def test_ollama_import():
    """Testa l'importazione della libreria ollama"""
    try:
        import ollama
        print("✅ Libreria ollama importata correttamente")
        
        # Test veloce
        models = ollama.list()
        print(f"✅ API ollama funzionante - {len(models.models)} modelli")
        return True
    except ImportError:
        print("❌ Libreria ollama non trovata")
        print("   Installa con: pip install ollama")
        return False
    except Exception as e:
        print(f"❌ Errore nella libreria ollama: {e}")
        return False

def test_quick_generation():
    """Test veloce di generazione"""
    try:
        import ollama
        
        # Trova un modello Granite disponibile
        models = ollama.list()
        granite_model = None
        
        for model in models.models:
            if 'granite' in model.model.lower():
                granite_model = model.model
                break
        
        if not granite_model:
            print("❌ Nessun modello Granite disponibile per il test")
            return False
        
        print(f"🧪 Test generazione con {granite_model}...")
        response = ollama.generate(
            model=granite_model,
            prompt="Dimmi solo 'Ciao!' in una parola"
        )
        
        print(f"✅ Test completato! Risposta: {response['response'].strip()}")
        return True
        
    except Exception as e:
        print(f"❌ Errore nel test di generazione: {e}")
        return False

def main():
    """Esegue tutti i test di configurazione"""
    print("🔧 Verifica configurazione Ollama + Python")
    print("=" * 50)
    
    tests = [
        ("Versione Python", check_python_version),
        ("Server Ollama", check_ollama_server),
        ("Modelli Granite", check_granite4_model),
        ("Libreria Python", test_ollama_import),
        ("Test generazione", test_quick_generation)
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\n📋 {name}:")
        success = test_func()
        results.append((name, success))
    
    print("\n" + "=" * 50)
    print("📊 RISULTATI:")
    
    all_passed = True
    for name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} - {name}")
        if not success:
            all_passed = False
    
    if all_passed:
        print("\n🎉 Tutto configurato correttamente!")
        print("   Puoi iniziare a usare gli script di esempio.")
    else:
        print("\n⚠️  Alcuni test sono falliti.")
        print("   Controlla i messaggi di errore sopra.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)