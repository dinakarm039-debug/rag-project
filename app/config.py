
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-4o"

    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")

    AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
    AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")

settings = Settings()
