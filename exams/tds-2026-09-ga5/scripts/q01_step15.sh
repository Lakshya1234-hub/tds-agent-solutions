cat << 'EOF' > /home/lakshyadeep/tds-agent/workspace/solve_q1.py
import json
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import numpy as np

app = FastAPI()

with open('/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json') as f:
    passages = json.load(f)

class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3

class QueryResponse(BaseModel):
    answer: Optional[str]
    sources: List[int]
    scores: List[float]
    confidence: float

@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    q = req.question.lower()
    # Simple keyword/token matching or TF-IDF / embedding heuristic
    scores = []
    q_words = set(q.split())
    for i, p in enumerate(passages):
        p_lower = p.lower()
        p_words = set(p_lower.split())
        common = q_words.intersection(p_words)
        score = len(common) / (len(q_words) + 1e-5)
        # boost for exact phrase or matching numbers
        for w in q_words:
            if len(w) > 3 and w in p_lower:
                score += 0.2
        scores.append((score, i))
    
    scores.sort(key=lambda x: x[0], reverse=True)
    top_k = req.top_k or 3
    top_items = scores[:top_k]
    
    chosen_sources = [item[1] for item in top_items]
    chosen_scores = [float(item[0]) for item in top_items]
    confidence = float(chosen_scores[0]) if chosen_scores else 0.0
    
    # Generate answer from top passage or abstain if confidence too low
    if confidence < 0.05:
        answer = None
    else:
        answer = passages[chosen_sources[0]]
        
    return {
        "answer": answer,
        "sources": chosen_sources,
        "scores": chosen_scores,
        "confidence": min(max(confidence, 0.0), 1.0)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
EOF
python3 -c "print('Script written')"
