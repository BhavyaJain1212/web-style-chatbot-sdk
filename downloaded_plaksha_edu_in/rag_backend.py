import os
import re
from bs4 import BeautifulSoup
from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Setup API Key (hardcoded for convenience)
os.environ["OPENAI_API_KEY"] = "ADD API KEY"

# Helper function to clean up the messy HTML scraped from the web
def bs4_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    # Remove excessive blank lines
    return re.sub(r"\n\n+", "\n\n", soup.text).strip()

def build_rag_pipeline(target_url):
    print(f"Scraping data from {target_url}...")
    
    # 2. Load Data: Scrapes the root URL and its child links
    # max_depth=2 prevents the scraper from getting stuck in an infinite loop
    loader = RecursiveUrlLoader(
        target_url,
        max_depth=2, 
        extractor=bs4_extractor
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} pages.")

    # 3. Split Text: Breaks pages into 1000-character chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200 # Overlap prevents cutting sentences in half
    )
    splits = text_splitter.split_documents(docs)

    # 4. Vector Store: Converts chunks to numbers and stores them locally
    print("Creating vector store (this might take a moment)...")
    vectorstore = Chroma.from_documents(
        documents=splits, 
        embedding=OpenAIEmbeddings(),
        persist_directory="./website_chroma_db"
    )
    
    # The retriever acts as the search engine for our database
    retriever = vectorstore.as_retriever()

    # 5. Create the AI Chain
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Instruct the AI on how to behave
    system_prompt = (
        "You are an intelligent assistant for the website. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # Link the document processing and the retriever together
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

# --- Usage ---
if __name__ == "__main__":
    # Insert the target URL you want to scrape here
    website_url = "https://plaksha.edu.in/" 
    
    chatbot_chain = build_rag_pipeline(website_url)
    
    # Simple terminal interface to test your bot
    print("\n--- Pipeline Ready ---")
    print("Type 'exit' to quit.")
    
    while True:
        user_query = input("\nYou: ")
        if user_query.lower() == 'exit':
            break
            
        # The invoke method searches the vector store and generates the answer
        response = chatbot_chain.invoke({"input": user_query})
        print(f"\nBot: {response['answer']}")