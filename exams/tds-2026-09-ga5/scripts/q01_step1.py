import json
import os

with open("/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json") as f:
    kb = json.load(f)

print(f"Loaded {len(kb)} passages from knowledge base.")
print(kb[0])
