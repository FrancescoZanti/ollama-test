#!/usr/bin/env python3
"""
Test script per verificare la configurazione del server Ollama tramite .env
"""

import os
import sys
import subprocess
from pathlib import Path

def run_python_code(code):
    """Esegue codice Python in un processo isolato"""
    result = subprocess.run(
        [sys.executable, '-c', code],
        capture_output=True,
        text=True,
        cwd=os.getcwd()
    )
    if result.returncode != 0:
        raise RuntimeError(f"Error: {result.stderr}")
    return result.stdout.strip()

def test_config_module():
    """Test del modulo config"""
    print("🧪 Test modulo config...")
    
    # Test 1: Default value quando .env non esiste
    if Path('.env').exists():
        os.remove('.env')
    
    url = run_python_code('from config import get_ollama_base_url; print(get_ollama_base_url())')
    assert url == 'http://localhost:11434', f"Expected default URL, got {url}"
    print("  ✅ Test 1: URL default corretto")
    
    # Test 2: URL personalizzato da .env
    with open('.env', 'w') as f:
        f.write('OLLAMA_BASE_URL=http://test-server:9999\n')
    
    url = run_python_code('from config import get_ollama_base_url; print(get_ollama_base_url())')
    assert url == 'http://test-server:9999', f"Expected custom URL, got {url}"
    print("  ✅ Test 2: URL personalizzato da .env corretto")
    
    # Cleanup
    os.remove('.env')
    print("✅ Tutti i test del modulo config superati\n")

def test_http_client():
    """Test del client HTTP"""
    print("🧪 Test OllamaHTTPClient...")
    
    # Cleanup any .env file first
    if Path('.env').exists():
        os.remove('.env')
    
    # Test con default
    url = run_python_code('''
from ollama_http import OllamaHTTPClient
client = OllamaHTTPClient()
print(client.base_url)
''')
    assert url == 'http://localhost:11434', f"Expected default, got {url}"
    print("  ✅ Test 1: Client con URL default")
    
    # Test con URL personalizzato
    url = run_python_code('''
from ollama_http import OllamaHTTPClient
client = OllamaHTTPClient(base_url='http://custom:8080')
print(client.base_url)
''')
    assert url == 'http://custom:8080', f"Expected custom, got {url}"
    print("  ✅ Test 2: Client con URL personalizzato")
    
    print("✅ Tutti i test OllamaHTTPClient superati\n")

def test_advanced_client():
    """Test del client avanzato"""
    print("🧪 Test OllamaClient...")
    
    # Cleanup any .env file first
    if Path('.env').exists():
        os.remove('.env')
    
    # Test con default
    url = run_python_code('''
from ollama_advanced import OllamaClient
client = OllamaClient()
print(client.base_url)
''')
    assert url == 'http://localhost:11434', f"Expected default, got {url}"
    print("  ✅ Test 1: Client con URL default")
    
    # Test con URL personalizzato
    url = run_python_code('''
from ollama_advanced import OllamaClient
client = OllamaClient(base_url='http://custom:7777')
print(client.base_url)
''')
    assert url == 'http://custom:7777', f"Expected custom, got {url}"
    print("  ✅ Test 2: Client con URL personalizzato")
    
    print("✅ Tutti i test OllamaClient superati\n")

def test_env_file_ignored():
    """Test che .env sia ignorato da git"""
    print("🧪 Test .gitignore...")
    
    import subprocess
    
    # Crea un file .env
    with open('.env', 'w') as f:
        f.write('OLLAMA_BASE_URL=http://test:1234\n')
    
    # Verifica che sia ignorato
    result = subprocess.run(
        ['git', 'status', '--short'],
        capture_output=True,
        text=True
    )
    
    if '.env' in result.stdout:
        print("  ❌ Errore: .env non è ignorato da git")
        os.remove('.env')
        sys.exit(1)
    
    print("  ✅ File .env correttamente ignorato da git")
    
    # Cleanup
    os.remove('.env')
    print("✅ Test .gitignore superato\n")

def test_env_example_exists():
    """Test che .env.example esista"""
    print("🧪 Test .env.example...")
    
    assert Path('.env.example').exists(), ".env.example non trovato"
    print("  ✅ File .env.example esiste")
    
    # Verifica che contenga OLLAMA_BASE_URL
    with open('.env.example', 'r') as f:
        content = f.read()
    
    assert 'OLLAMA_BASE_URL' in content, ".env.example deve contenere OLLAMA_BASE_URL"
    print("  ✅ File .env.example contiene OLLAMA_BASE_URL")
    
    print("✅ Test .env.example superato\n")

def main():
    """Esegue tutti i test"""
    print("=" * 60)
    print("🔧 Test configurazione server Ollama tramite .env")
    print("=" * 60 + "\n")
    
    try:
        test_env_example_exists()
        test_config_module()
        test_http_client()
        test_advanced_client()
        test_env_file_ignored()
        
        print("=" * 60)
        print("🎉 TUTTI I TEST SUPERATI!")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test fallito: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Errore imprevisto: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
