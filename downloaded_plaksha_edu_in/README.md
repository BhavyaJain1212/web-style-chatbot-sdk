# Plaksha University RAG Chatbot

A web-based chatbot that scrapes data from the Plaksha University website and answers questions using Retrieval-Augmented Generation (RAG) powered by LangChain and OpenAI.

## Project Overview

This project consists of three main components:

1. **rag_backend.py** - Scrapes the Plaksha website and builds a vector store using LangChain
2. **app.py** - FastAPI server that provides a `/chat` endpoint for chatbot interactions
3. **index.html** - Interactive web interface with a floating chatbot widget

## Architecture

```
┌─────────────────────────────────────────┐
│     Web Browser (index.html)            │
│   ┌─────────────────────────────────┐   │
│   │  Floating Chatbot Widget        │   │
│   │  - Chat UI                      │   │
│   │  - Message handling            │   │
│   │  - Sends POST /chat requests    │   │
│   └─────────────────────────────────┘   │
└────────┬────────────────────────────────┘
         │ HTTP POST /chat
         ▼
┌─────────────────────────────────────────┐
│  FastAPI Server (app.py)                │
│  ┌─────────────────────────────────┐   │
│  │  /chat Endpoint                 │   │
│  │  - Receives user message        │   │
│  │  - Calls RAG pipeline           │   │
│  │  - Returns bot response         │   │
│  └─────────────────────────────────┘   │
└────────┬────────────────────────────────┘
         │ Uses
         ▼
┌─────────────────────────────────────────┐
│  RAG Pipeline (rag_backend.py)          │
│  ┌─────────────────────────────────┐   │
│  │  1. Web Scraper                 │   │
│  │     - Scrapes plaksha.edu.in    │   │
│  │     - Extracts text content     │   │
│  │  2. Text Splitter               │   │
│  │     - Chunks into 1000 chars    │   │
│  │     - 200 char overlap          │   │
│  │  3. Vector Store (Chroma)       │   │
│  │     - Stores embeddings         │   │
│  │     - Persists to disk          │   │
│  │  4. Retrieval Chain             │   │
│  │     - Retrieves relevant docs   │   │
│  │     - Uses GPT-3.5 Turbo        │   │
│  │     - Generates response        │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

## Prerequisites

- Python 3.8+
- OpenAI API Key (get from https://platform.openai.com/api-keys)
- Internet connection (for scraping website and API calls)

## Installation

### 1. Clone/Download the Repository

```bash
cd c:\Users\Sohan\AppData\Local\Programs\Python\Python312\ai_prod_design_2026\downloaded_plaksha_edu_in
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install langchain langchain-community langchain-openai langchain-text-splitters beautifulsoup4 fastapi uvicorn pydantic chromadb
```

## Configuration

### Set OpenAI API Key

You need to set your OpenAI API key as an environment variable:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your-openai-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-api-key-here
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

## Running the Application

### Step 1: Start the FastAPI Backend Server

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Or simply:
```bash
uvicorn app:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Initializing RAG Pipeline... (This may take a minute)
INFO:     Scraping data from https://plaksha.edu.in/...
INFO:     Loaded 45 pages.
INFO:     Creating vector store (this might take a moment)...
INFO:     Server is ready!
```

⏸️ **Note:** The first run will take 1-2 minutes to scrape the website and build the vector store.

### Step 2: Open the Frontend

Open `index.html` in your web browser:

**Option 1 - Direct File:**
```
file:///c:/Users/Sohan/AppData/Local/Programs/Python/Python312/ai_prod_design_2026/downloaded_plaksha_edu_in/index.html
```

**Option 2 - Python Web Server:**
```bash
python -m http.server 8001
```
Then visit: `http://localhost:8001`

### Step 3: Use the Chatbot

1. Click the floating chat button (💬) in the bottom-right corner
2. Type your question about Plaksha University
3. Press Enter or click Send
4. Wait for the bot's response (first response may take 5-10 seconds)

## Example Questions

- "What are the BTech programs offered at Plaksha?"
- "How do I apply for admissions?"
- "Tell me about the campus facilities"
- "What scholarships are available?"
- "When are the application deadlines?"

## How It Works

### Data Flow

1. **User asks a question** via the web interface
2. **Frontend sends** the message to the FastAPI server via `POST /chat`
3. **Backend RAG Pipeline:**
   - Searches the vector store for relevant Plaksha content
   - Retrieves the top matching documents
   - Sends documents + question to GPT-3.5 Turbo
   - Returns generated answer
4. **Frontend receives** the response and displays it in the chat

### RAG (Retrieval-Augmented Generation)

Instead of just using the LLM's training data, RAG:
- Retrieves specific content from a knowledge base (Plaksha website)
- Provides this context to the LLM
- LLM generates answers based on actual website content
- Results are more accurate and up-to-date

## File Structure

```
downloaded_plaksha_edu_in/
├── app.py                      # FastAPI server
├── rag_backend.py              # RAG pipeline logic
├── index.html                  # Web interface with chatbot
├── requirements.txt            # Python dependencies
├── chatwithus.css             # Chatbot styling
├── styles.css                 # General page styling
├── website_chroma_db/         # Vector store (created on first run)
└── README.md                  # This file
```

## Troubleshooting

### Error: "OPENAI_API_KEY environment variable not set"
**Solution:** Set your OpenAI API key (see Configuration section)

### Error: "Could not connect to the server"
**Solution:** Make sure FastAPI server is running on `http://localhost:8000`

### Slow First Response
**Normal behavior** - The first response takes time because:
- Backend is loading the RAG pipeline
- Vector search is retrieving relevant documents
- LLM is generating response

Subsequent responses are much faster (typically 2-5 seconds).

### Vector Store Already Exists
If you want to rebuild the vector store:
```bash
rmdir /s website_chroma_db   # Windows
rm -rf website_chroma_db     # Mac/Linux
```

Then restart the server.

## Customization

### Change Website to Scrape
Edit `rag_backend.py`:
```python
TARGET_URL = "https://your-website.com/"  # Change this
```

### Adjust Chatbot Appearance
Edit the CSS in `index.html` (lines 6400-6560):
```javascript
--plaksha-teal: #008B8B;    // Color
--chat-width: 350px;        // Width
```

### Change Server Port
Run with different port:
```bash
uvicorn app:app --port 8080
```

And update the fetch URL in `index.html`:
```javascript
const response = await fetch('http://localhost:8080/chat', {
```

## API Documentation

### Endpoint: POST /chat

**Request:**
```json
{
  "message": "What are the admission requirements?"
}
```

**Response:**
```json
{
  "reply": "Based on Plaksha's admission requirements..."
}
```

## Performance Notes

- **Initialization:** 1-2 minutes (first run only)
- **RAG Response Time:** 2-10 seconds per query
- **Vector Store Size:** ~50-100 MB (depending on website size)

## Limitations

- Only answers questions based on Plaksha website content
- Responses are limited to what's publicly available on the website
- May have hallucinations if context is ambiguous
- Rate limited by OpenAI API (free tier has limits)

## License

Created for educational purposes.

## Support

For issues or questions:
1. Check Troubleshooting section above
2. Verify all files are in the correct directory
3. Check that Python packages are installed: `pip list`
4. Verify OpenAI API key is valid and has sufficient credits
5. Check browser console for JavaScript errors (F12)

---

**Happy chatting! 🤖**
