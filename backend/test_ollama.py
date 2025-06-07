import requests

def test_ollama():
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": "Hello, are you working?",
                "stream": False
            }
        )
        if response.status_code == 200:
            print("Success! Ollama is working!")
            print("Response:", response.json())
        else:
            print(f"Error: Ollama returned status code {response.status_code}")
    except Exception as e:
        print(f"Error connecting to Ollama: {str(e)}")

if __name__ == "__main__":
    test_ollama() 