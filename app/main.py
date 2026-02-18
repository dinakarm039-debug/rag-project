
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="RAG Chatbot")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "running"}
