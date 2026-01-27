import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

DATA_PATH = "data/personal_profile.txt"
DB_PATH = "vector_db/chroma"

# Load environment variables from .env
load_dotenv()

def ingest():
    print("📄 Loading personal profile...")
    loader = TextLoader(DATA_PATH, encoding="utf-8")
    documents = loader.load()

    print("✂️ Splitting text...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )
    chunks = splitter.split_documents(documents)

    print("🧠 Creating embeddings...")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        api_key=api_key
    )

    print("💾 Saving into ChromaDB...")
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("✅ RAG ingestion completed!")

if __name__ == "__main__":
    ingest()
