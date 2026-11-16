from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Load the knowledge base
with open('/home/lakshyadeep/tds-agent-offline/workspace/downloads/q1_knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    question = data.get("question")
    top_k = data.get("top_k", 3)

    if not question:
        return JSONResponse(content={"error": "Question is required"}, status_code=400)

    # Dummy implementation for demonstration purposes
    answer = None
    sources = []
    scores = []
    confidence = 0.0

    # TODO: Implement RAG logic here

    return JSONResponse(content={
        "answer": answer,
        "sources": sources,
        "scores": scores,
        "confidence": confidence
    })

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
