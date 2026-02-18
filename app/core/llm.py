
from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """

You are a strict RAG assistant.

Rules:
- Answer ONLY from provided context
- If answer not in context say: "I don't know based on the provided documents"
- Do not hallucinate
- Be accurate and concise

"""

class LLM:

    def generate(self, question, context):

        response = client.chat.completions.create(

            model=settings.OPENAI_MODEL,

            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},

                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion:\n{question}"
                }
            ]

        )

        return response.choices[0].message.content
