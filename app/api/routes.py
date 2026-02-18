
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.rag_engine import RAGEngine

router = APIRouter()

rag = RAGEngine()

class QueryRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(req: QueryRequest):

    answer = rag.ask(req.question)

    return {
        "question": req.question,
        "answer": answer
    }
