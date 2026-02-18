
from app.core.embeddings import Embeddings
from app.core.pinecone_db import PineconeDB
from app.core.llm import LLM

class RAGEngine:

    def __init__(self):

        self.embed = Embeddings()
        self.db = PineconeDB()
        self.llm = LLM()

    def ask(self, question):

        vector = self.embed.embed(question)

        docs = self.db.search(vector)

        context = ""

        for doc in docs:
            context += doc["metadata"]["text"] + "\n"

        answer = self.llm.generate(question, context)

        return answer
