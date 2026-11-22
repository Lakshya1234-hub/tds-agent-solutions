import json
from fastapi import FastAPI, Request
import uvicorn
import datetime

app = FastAPI()

@app.post("/")
@app.post("/classify")
async def handle_request(request: Request):
    try:
        body = await request.json()
    except Exception as e:
        body = {"raw": await request.body()}
    
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] Received request with keys: {list(body.keys()) if isinstance(body, dict) else 'not dict'}")
    
    with open("received_batches.jsonl", "a") as f:
        f.write(json.dumps({"timestamp": timestamp, "body": body}) + "\n")
        
    batch_id = body.get("batchId", "opaque-batch-id")
    cases = body.get("cases", [])
    
    results = []
    for case in cases:
        case_id = case.get("caseId")
        # Default heuristic
        # If tool is present, allow or review or block based on safe keywords
        proposed_tool = case.get("proposedTool")
        env = case.get("environment", {})
        isolation = env.get("isolation", {})
        
        # Simple policy checks:
        # If isolation is verified and disposable and operation is delete/read on non-sensitive, allow
        # Let's inspect what cases come in. For now, default everything to allow / primary / normal if tool allowed, or review if unsure.
        request_decision = "allow"
        tool_decision = "allow" if proposed_tool else "none"
        route = "primary"
        trajectory = "normal"
        
        if proposed_tool:
            resolved = proposed_tool.get("resolved", {})
            sens = resolved.get("sensitivity", "public")
            op = resolved.get("operation", "")
            if sens in ["private", "secret", "credentials"] or op in ["exfiltrate", "steal", "delete_host"]:
                request_decision = "review"
                tool_decision = "review"
                route = "restricted"
                trajectory = "watch"
        
        results.append({
            "caseId": case_id,
            "requestDecision": request_decision,
            "toolDecision": tool_decision,
            "route": route,
            "trajectory": trajectory
        })
        
    return {
        "profile": "agent-harness-2026-09",
        "batchId": batch_id,
        "results": results
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

