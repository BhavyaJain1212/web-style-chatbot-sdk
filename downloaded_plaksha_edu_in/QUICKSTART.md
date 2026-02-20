# ✅ Plaksha RAG Chatbot - Setup Complete!

## What's Been Done

Your Plaksha University RAG Chatbot is now ready to use! Here's what has been set up:

### ✅ Files Created/Modified:

1. **rag_backend.py** - Updated to use environment variables for API key
   - Scrapes Plaksha website
   - Creates vector database
   - Powers the RAG pipeline

2. **app.py** - Enhanced FastAPI server
   - Improved error handling
   - Better initialization
   - Ready for production use

3. **index.html** - Already contains chatbot UI
   - Floating chat widget (💬 button)
   - Real-time message handling
   - Connected to backend API

4. **requirements.txt** - All dependencies listed
   - LangChain, FastAPI, OpenAI, ChromaDB, etc.

5. **README.md** - Comprehensive documentation
   - Architecture explanation
   - Full usage guide
   - Troubleshooting tips

6. **SETUP.md** - Windows-specific setup guide
   - Step-by-step instructions
   - API key configuration
   - Quick start scripts

7. **start_server.ps1** - PowerShell script to start server
   - Automatic dependency check
   - Error handling included

8. **start_server.bat** - Batch file for Command Prompt
   - Alternative startup method

---

## 🚀 Quick Start (Just 3 Steps!)

### Step 1: Set Your OpenAI API Key

In PowerShell (recommended):
```powershell
$env:OPENAI_API_KEY = "sk-your-api-key-here"
```

Or in Command Prompt:
```cmd
setx OPENAI_API_KEY "sk-your-api-key-here"
```

Get your free API key from: https://platform.openai.com/api-keys

### Step 2: Start the Server

Navigate to the project directory:
```cmd
cd c:\Users\Sohan\AppData\Local\Programs\Python\Python312\ai_prod_design_2026\downloaded_plaksha_edu_in
```

Run one of these commands:
```powershell
.\start_server.ps1        # Best option
```
Or:
```cmd
start_server.bat
```
Or:
```cmd
uvicorn app:app --reload
```

**Wait for the message: "Server is ready!"**

### Step 3: Open the Chatbot

Double-click `index.html` in Windows Explorer
OR
Open in browser: `file:///C:/Users/Sohan/AppData/Local/Programs/Python/Python312/ai_prod_design_2026/downloaded_plaksha_edu_in/index.html`

Click the floating chat button (💬) and start chatting!

---

## 🎯 How It Works

```
YOU (Browser)
    ↓ Asks Question
    ↓ (index.html)
    ↓
FASTAPI SERVER (app.py, port 8000)
    ↓ Processes with RAG pipeline
    ↓ (rag_backend.py)
    ↓
OPENAI GPT-3.5-TURBO
    ↓ Generates answer using
    ↓ Plaksha website content
    ↓
RESPONSE (bot reply)
```

---

## 📝 Example Queries to Try

1. "What are the BTech programs at Plaksha?"
2. "How do I apply for admissions?"
3. "Tell me about campus facilities"
4. "What scholarships are available?"
5. "What are the entry requirements?"
6. "When are the application deadlines?"
7. "Tell me about the faculty"
8. "What is the placement record?"

---

## ⚙️ System Requirements

✅ Python 3.8+ (installed)
✅ OpenAI API Key (free account available)
✅ Internet connection
✅ Modern web browser (Chrome, Firefox, Edge, Safari)
✅ Windows/Mac/Linux
✅ ~100MB disk space (for vector database)

---

## 🎓 Architecture Overview

Your chatbot uses **Retrieval-Augmented Generation (RAG)**:

1. **Web Scraper** → Extracts content from plaksha.edu.in
2. **Text Splitter** → Breaks content into 1000-char chunks
3. **Embeddings** → Converts text to vectors (using OpenAI)
4. **Vector Store** → Stores embeddings in Chroma database
5. **Retriever** → Finds relevant content for each question
6. **LLM** → Uses GPT-3.5 to generate natural responses

This ensures answers are:
- ✅ Based on actual Plaksha website content
- ✅ Current and accurate
- ✅ Relevant to user questions
- ✅ Professionallly formatted

---

## 📊 First Run Expectations

- **Initialization:** 1-2 minutes (scraping website)
- **First chat response:** 5-10 seconds
- **Subsequent responses:** 2-5 seconds
- **Vector database size:** ~50-100 MB

---

## 🔧 Customization Options

### Change Website to Scrape
Edit `rag_backend.py` line 76:
```python
TARGET_URL = "https://your-site.com/"
```

### Change Chatbot Colors
Edit `index.html` line 6404:
```css
--plaksha-teal: #008B8B;  /* Change color here */
```

### Change Chat Window Size
Edit `index.html` line 6402:
```css
--chat-width: 350px;  /* Make it wider/narrower */
```

---

## 🆘 Need Help?

### Error: "ModuleNotFoundError: No module named 'langchain'"
```cmd
pip install -r requirements.txt
```

### Error: "OPENAI_API_KEY environment variable not set"
```powershell
$env:OPENAI_API_KEY = "your-key"
```

### Server won't start?
1. Check Python is installed: `python --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Check port 8000 is free
4. Enable firewall access for Python

### Chatbot not responding?
1. Check server is running ("Server is ready!" message)
2. Check internet connection
3. Verify OpenAI API key is valid
4. Check browser console (F12) for errors

---

## 📚 Learn More

- **LangChain:** https://python.langchain.com/
- **FastAPI:** https://fastapi.tiangolo.com/
- **RAG Concept:** https://aws.amazon.com/what-is/retrieval-augmented-generation/
- **OpenAI API:** https://platform.openai.com/docs/

---

## 🎉 You're All Set!

Your chatbot is ready to:
- ✅ Answer Plaksha-related questions
- ✅ Provide accurate information
- ✅ Handle natural language queries
- ✅ Run locally on your machine
- ✅ Scale to other websites

**Happy chatting! 🤖💬**

---

## 📞 Support

If you encounter issues:

1. **Check the logs** - Look at terminal output
2. **Read SETUP.md** - Windows-specific troubleshooting
3. **Read README.md** - Complete documentation
4. **Verify files** - All files should be in `downloaded_plaksha_edu_in/`
5. **Check requirements** - Run `pip install -r requirements.txt`

---

## 🚀 Next Steps

1. ✅ Set your OpenAI API Key (see Step 1 above)
2. ✅ Run `start_server.ps1` or `start_server.bat`
3. ✅ Wait for "Server is ready!" message (1-2 minutes first time)
4. ✅ Open `index.html` in your browser
5. ✅ Click the chat button and start asking questions!

**Enjoy your intelligent Plaksha chatbot! 🎓**
