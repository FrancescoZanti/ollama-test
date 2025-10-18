#!/usr/bin/env python3
"""
Interazione con Ollama usando richieste HTTP dirette
"""

import requests
import json
from typing import Dict, Any, Iterator

class OllamaHTTPClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip('/')
    
    def list_models(self) -> Dict[str, Any]:
        """Lista tutti i modelli disponibili"""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def generate(self, model: str, prompt: str, stream: bool = False) -> Dict[str, Any]:
        """Genera una risposta usando l'API /api/generate"""
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                stream=stream
            )
            response.raise_for_status()
            
            if stream:
                return self._handle_streaming_response(response)
            else:
                return response.json()
                
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def chat(self, model: str, messages: list, stream: bool = False) -> Dict[str, Any]:
        """Chat usando l'API /api/chat"""
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                stream=stream
            )
            response.raise_for_status()
            
            if stream:
                return self._handle_streaming_response(response)
            else:
                return response.json()
                
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def _handle_streaming_response(self, response) -> Iterator[Dict[str, Any]]:
        """Gestisce le risposte in streaming"""
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue
    
    def embeddings(self, model: str, prompt: str) -> Dict[str, Any]:
        """Genera embeddings per un testo"""
        payload = {
            "model": model,
            "prompt": prompt
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/embeddings",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

def test_http_client():
    """Testa il client HTTP"""
    client = OllamaHTTPClient()
    
    print("=== Lista modelli ===")
    models = client.list_models()
    if "error" not in models:
        for model in models.get("models", []):
            print(f"- {model['name']}")
    else:
        print(f"Errore: {models['error']}")
    
    print("\n=== Generazione semplice ===")
    result = client.generate("granite4", "Scrivi una breve barzelletta")
    if "error" not in result:
        print(f"Risposta: {result['response']}")
    else:
        print(f"Errore: {result['error']}")
    
    print("\n=== Chat ===")
    messages = [
        {"role": "user", "content": "Ciao! Come stai?"}
    ]
    result = client.chat("granite4", messages)
    if "error" not in result:
        print(f"Risposta: {result['message']['content']}")
    else:
        print(f"Errore: {result['error']}")
    
    print("\n=== Streaming ===")
    print("Risposta in streaming:")
    stream_result = client.generate("granite4", "Conta da 1 a 5 lentamente", stream=True)
    if hasattr(stream_result, '__iter__'):
        for chunk in stream_result:
            if 'response' in chunk:
                print(chunk['response'], end='', flush=True)
        print()  # Nuova riga

if __name__ == "__main__":
    test_http_client()