# PrivChat – PII Detection & LLM Chat

PrivChat is a modern web application for detecting and highlighting Personally Identifiable Information (PII) in user prompts, and for interacting with a local Large Language Model (LLM) via Ollama. It features a beautiful chat UI, real-time PII highlighting, and a robust FastAPI backend.

---

## Features
- **Real-time PII Detection** using spaCy NER
- **Local LLM Integration** via Ollama REST API
- **Modern Chat UI** with PII highlights and LLM responses
- **Multi-chat spaces** (switch between conversations)
- **Industry-grade UX**: loading spinners, error handling, responsive design

---

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **PII Detection:** spaCy (`en_core_web_sm`)
- **LLM:** Ollama (e.g., `llama2`)

---

## Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- (Optional) Node.js for advanced frontend tooling

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/privchat.git
cd privchat
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Start Ollama & Download Model
Make sure [Ollama](https://ollama.ai/) is installed and running:
```bash
ollama serve
ollama pull llama2
```

### 4. Start the FastAPI Backend
```bash
uvicorn app.main:app --reload
```

### 5. Frontend Setup & Launch
You can use Python's built-in server:
```bash
cd ..
python -m http.server 8080
```
Then open [http://localhost:8080/chatpage.html](http://localhost:8080/chatpage.html) in your browser.

---

## Usage
1. Enter your prompt in the chat input and click **Send**.
2. Detected PII will be highlighted and listed below your message.
3. The LLM response will appear in the right panel. For long responses, click **Read more** to open the full answer in a new tab.
4. Switch between chat spaces to manage multiple conversations.

---

## Project Structure
```
privchat/
├── backend/
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── chatpage.html
├── .gitignore
└── README.md
```

## Troubleshooting
- **Ollama not running?** Make sure you've started `ollama serve` and pulled the model.
- **Backend errors?** Check your FastAPI logs for Python or spaCy errors.
- **Frontend not updating?** Make sure you're using a modern browser and have no JS errors in the console.

---

## Contact
For questions or support, open an issue or contact the maintainer via GitHub.

