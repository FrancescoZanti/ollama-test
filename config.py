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

def get_ollama_base_url() -> str:
    """
    Restituisce l'URL base del server Ollama
    
    Returns:
        str: URL del server Ollama (default: http://localhost:11434)
    """
    return OLLAMA_BASE_URL
