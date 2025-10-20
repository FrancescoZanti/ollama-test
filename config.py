#!/usr/bin/env python3
"""
Modulo di configurazione per caricare le variabili d'ambiente
"""

import os
from dotenv import load_dotenv

# Carica le variabili dal file .env se presente
load_dotenv()

# Configurazione Ollama
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')

# Imposta OLLAMA_HOST per compatibilità con la libreria ollama
# La libreria ollama usa OLLAMA_HOST, quindi lo impostiamo se non è già definito
if 'OLLAMA_HOST' not in os.environ:
    os.environ['OLLAMA_HOST'] = OLLAMA_BASE_URL

def get_ollama_base_url() -> str:
    """
    Restituisce l'URL base del server Ollama
    
    Returns:
        str: URL del server Ollama (default: http://localhost:11434)
    """
    return OLLAMA_BASE_URL
