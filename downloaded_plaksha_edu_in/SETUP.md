# Windows Setup Guide - Plaksha RAG Chatbot

## ✅ Quick Start (5 minutes)

### Step 1: Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (keep it safe!)

### Step 2: Set Environment Variable

**Option A: Using PowerShell (Recommended)**

1. Open PowerShell (right-click on terminal, select "Run as administrator")
2. Copy and run this command:
   ```powershell
   $env:OPENAI_API_KEY = "sk-...paste-your-api-key-here..."
   ```
3. Verify it's set:
   ```powershell
   $env:OPENAI_API_KEY
   ```

**Option B: Using Command Prompt**

1. Open Command Prompt (Win+R, type `cmd`, press Enter)
2. Run this command:
   ```cmd
   setx OPENAI_API_KEY "sk-...paste-your-api-key-here..."
   ```
3. **Close and reopen Command Prompt** for changes to take effect
4. Verify it's set:
   ```cmd
   echo %OPENAI_API_KEY%
   ```

**Option C: Permanent Environment Variable (Persists Across Restarts)**

1. Press `Win+R` and type `sysdm.cpl`
2. Click "Environment Variables" button
3. Click "New" under "User variables"
4. Variable name: `OPENAI_API_KEY`
5. Variable value: `sk-...your-api-key...`
6. Click OK and close all dialogs
7. **Restart your terminal or IDE** for changes to take effect

### Step 3: Install Dependencies

1. Open PowerShell or Command Prompt in the project directory:
   ```cmd
   cd c:\Users\Sohan\AppData\Local\Programs\Python\Python312\ai_prod_design_2026\downloaded_plaksha_edu_in
   ```

2. Run:
   ```cmd
   pip install -r requirements.txt
   ```

### Step 4: Start the Server

1. **Using PowerShell Script (Easiest):**
   ```powershell
   .\start_server.ps1
   ```

2. **Or Using Batch File:**
   ```cmd
   start_server.bat
   ```

3. **Or Manually:**
   ```cmd
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Initializing RAG Pipeline...
INFO:     Scraping data from https://plaksha.edu.in/...
INFO:     Loaded XX pages...
INFO:     Creating vector store...
INFO:     Server is ready!
```

⏸️ **First run takes 1-2 minutes to scrape and build the vector store**

### Step 5: Open the Chatbot

Open `index.html` in your web browser:
- **Direct file:** Double-click `index.html` in Windows Explorer
- **Or:** Type in address bar: `file:///C:/Users/Sohan/AppData/Local/Programs/Python/Python312/ai_prod_design_2026/downloaded_plaksha_edu_in/index.html`

Click the floating chat button (💬) in the bottom-right corner and start chatting!

---

## 🔧 Troubleshooting

### Problem: "OPENAI_API_KEY environment variable not set"

**Solution:**
1. Verify your API key is set by running in PowerShell:
   ```powershell
   $env:OPENAI_API_KEY
   ```
2. If empty, set it again (step 2 above)
3. If using permanent variable, restart your terminal/PowerShell

### Problem: "Cannot connect to server"

**Solution:**
1. Make sure server is running (you should see the "Uvicorn running" message)
2. Check that no other program is using port 8000
3. Try a different port:
   ```cmd
   uvicorn app:app --reload --port 8001
   ```
4. Update the fetch URL in `index.html` to match the new port

### Problem: "ModuleNotFoundError: No module named 'langchain'"

**Solution:**
1. Verify dependencies are installed:
   ```cmd
   pip list
   ```
2. Reinstall dependencies:
   ```cmd
   pip install --force-reinstall -r requirements.txt
   ```

### Problem: "Python is not recognized"

**Solution:**
1. Make sure Python is installed from https://www.python.org/
2. Add Python to PATH:
   - During installation, check "Add Python to PATH"
   - Or manually add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python312`

### Problem: Slow or no responses from chatbot

**Possible causes and solutions:**
1. **OpenAI API rate limit** - Wait a moment, try again
2. **API quota exceeded** - Check your OpenAI usage at https://platform.openai.com/usage/
3. **Slow internet** - The scraping and API calls need internet
4. **Server not ready** - Wait for initial "Server is ready!" message

### Problem: "The file format is not recognized"

When trying to run `.ps1` script:
1. Right-click on `start_server.ps1`
2. Select "Run with PowerShell"
3. If prompted about execution policy, type `Y` and press Enter

---

## 📁 Project Files

```
downloaded_plaksha_edu_in/
├── app.py                      # FastAPI backend (port 8000)
├── rag_backend.py              # RAG & web scraping logic
├── index.html                  # Web interface with chatbot
├── requirements.txt            # Python packages needed
├── README.md                   # Full documentation
├── SETUP.md                    # This file
├── .env.example                # Example environment config
├── start_server.bat            # Windows batch starter
├── start_server.ps1            # PowerShell starter
├── website_chroma_db/          # Vector database (created auto)
└── [other CSS files]           # Styling
```

---

## 🎯 What Each File Does

| File | Purpose |
|------|---------|
| **app.py** | Runs the chat server. Listens on http://localhost:8000 |
| **rag_backend.py** | Scrapes website and generates AI responses using RAG |
| **index.html** | Web page with chatbot interface & JavaScript |
| **rag_backend.py** | Manages embeddings, vector database, LLM interactions |
| **website_chroma_db/** | Stores vector embeddings (created automatically) |

---

## 🚀 Advanced Usage

### Use Different OpenAI Model

Edit `rag_backend.py` line ~65:
```python
llm = ChatOpenAI(model="gpt-4", temperature=0)  # Use GPT-4 instead
```

### Change Chat Server Port

```cmd
uvicorn app:app --port 9000
```

Then update in `index.html` (~line 6625):
```javascript
const response = await fetch('http://localhost:9000/chat', {
```

### Rebuild Vector Database

```cmd
rmdir /s website_chroma_db
```

Then restart the server. It will rebuild the database from scratch.

### Scrape Different Website

Edit `rag_backend.py` line ~76:
```python
TARGET_URL = "https://your-website.com/"
```

---

## 📊 Performance Notes

| Task | Time |
|------|------|
| First server start (scraping + indexing) | 1-2 minutes |
| Subsequent server starts | 10-30 seconds |
| First chat response | 5-10 seconds |
| Next responses | 2-5 seconds |

---

## ✨ Features

✅ Scrapes Plaksha University website automatically  
✅ Builds intelligent vector database (RAG)  
✅ Floating chatbot widget on any website  
✅ Real-time message streaming  
✅ Responsive design (works on mobile)  
✅ Natural language understanding  
✅ Context-aware responses  

---

## 🆘 Still Having Issues?

1. **Check logs** - Look at the terminal output for error messages
2. **Verify API key** - Make sure your OpenAI API key is valid
3. **Test API key** - Run a simple test in Python:
   ```python
   from openai import OpenAI
   client = OpenAI()
   print(client.models.list())
   ```
4. **Check dependencies** - Ensure all packages installed:
   ```cmd
   pip list | findstr langchain
   ```
5. **Check firewall** - Make sure port 8000 isn't blocked

---

## 📚 Additional Resources

- **LangChain Docs:** https://python.langchain.com/docs/get_started/introduction
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **OpenAI API Docs:** https://platform.openai.com/docs/
- **Uvicorn Docs:** https://www.uvicorn.org/

---

**Good luck! Happy chatting! 🚀**
