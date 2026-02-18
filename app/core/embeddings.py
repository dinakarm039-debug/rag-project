
from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class Embeddings:

    def embed(self, text):

        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=text
        )

        return response.data[0].embedding
