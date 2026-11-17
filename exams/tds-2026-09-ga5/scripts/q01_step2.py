import json

with open("/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json") as f:
    kb = json.load(f)

print("First 3 passages:")
for i in range(3):
    print(f"[{i}]: {kb[i][:100]}...")
