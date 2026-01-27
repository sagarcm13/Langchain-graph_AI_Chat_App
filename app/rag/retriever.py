import os
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

DB_PATH = "vector_db/chroma"
load_dotenv()


def get_relevant_context(query: str, k: int = 3) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        api_key=api_key
    )

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    docs = db.similarity_search(query, k=k)

    context = "\n\n".join([d.page_content for d in docs])
    return context
