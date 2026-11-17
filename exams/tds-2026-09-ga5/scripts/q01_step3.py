import json
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

with open("/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json") as f:
    passages = json.load(f)

vectorizer = TfidfVectorizer().fit(passages)
passage_vectors = vectorizer.transform(passages)

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

@app.post("/query")
def query_rag(req: QueryRequest):
    q_vec = vectorizer.transform([req.question])
    sims = cosine_similarity(q_vec, passage_vectors).flatten()
    top_indices = sims.argsort()[::-1][:req.top_k]
    
    scores = [float(sims[i]) for i in top_indices]
    
    # Simple extractive answer or synthesis
    # For now, return top passage text as answer or combined text
    best_idx = top_indices[0]
    answer = passages[best_idx]
    
    return {
        "answer": answer,
        "sources": [int(i) for i in top_indices],
        "scores": scores,
        "confidence": float(scores[0]) if scores else 0.0
    }

if __name__ == "__main__":
    import threading
    def run_server():
        uvicorn.run(app, host="127.0.0.1", port=8000)
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    print("RAG server started on port 8000")
