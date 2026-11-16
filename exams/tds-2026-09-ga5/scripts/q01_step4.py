import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Load the knowledge base
with open('/home/lakshyadeep/tds-agent-offline/workspace/downloads/q1_knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    question = data.get("question")
    top_k = data.get("top_k", 3)

    # Placeholder for actual query processing logic
    answer = None
    sources = []
    scores = []
    confidence = 0.0

    return {
        "answer": answer,
        "sources": sources,
        "scores": scores,
        "confidence": confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
