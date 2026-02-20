# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import sys

# Import the RAG pipeline function (Assuming you saved the previous Python script as 'rag_backend.py')
try:
    from rag_backend import build_rag_pipeline 
except ImportError as e:
    print(f"Error importing RAG backend: {e}", file=sys.stderr)
    raise

app = FastAPI()

# Enable CORS so your local HTML file can talk to this local server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the pipeline ONCE when the server starts
chatbot_chain = None

def initialize_rag():
    global chatbot_chain
    if chatbot_chain is None:
        print("Initializing RAG Pipeline... (This may take a minute)")
        TARGET_URL = "https://plaksha.edu.in/"
        try:
            chatbot_chain = build_rag_pipeline(TARGET_URL)
            print("Server is ready!")
        except Exception as e:
            print(f"Error initializing RAG pipeline: {e}", file=sys.stderr)
            raise

# Initialize on startup
initialize_rag()

# Define the data structure we expect from the frontend
class ChatRequest(BaseModel):
    message: str

# Create the API endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        if not chatbot_chain:
            return {"reply": "Chatbot is not initialized. Please try again later."}
        
        # Pass the user's message to the LangChain RAG pipeline
        response = chatbot_chain.invoke({"input": request.message})
        
        # Return the answer as JSON
        return {"reply": response['answer']}
    except Exception as e:
        print(f"Error in chat endpoint: {e}", file=sys.stderr)
        return {"reply": f"An error occurred: {str(e)}"}

# Route to serve static files (optional)
@app.get("/")
async def root():
    return {"message": "Plaksha RAG Chatbot API is running. Use POST /chat to send messages."}

# Run the server using: uvicorn app:app --reload
# Or for production: uvicorn app:app --host 0.0.0.0 --port 8000
