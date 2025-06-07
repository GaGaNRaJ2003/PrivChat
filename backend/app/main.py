from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

class PromptRequest(BaseModel):
    text: str

@app.post("/process")
async def process_prompt(request: PromptRequest):
    try:
        # spaCy NER
        doc = nlp(request.text)
        entities = [
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            }
            for ent in doc.ents
        ]
        # Ollama LLM
        ollama_response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": request.text,
                "stream": False
            }
        )
        if ollama_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Ollama API error")
        llm_response = ollama_response.json().get("response", "")
        return {
            "entities": entities,
            "llm_response": llm_response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "PrivChat API is running"} 