
from pinecone import Pinecone
from app.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

index = pc.Index(settings.PINECONE_INDEX)

class PineconeDB:

    def upsert(self, vectors):

        index.upsert(vectors)

    def search(self, vector):

        result = index.query(
            vector=vector,
            top_k=5,
            include_metadata=True
        )

        return result["matches"]
