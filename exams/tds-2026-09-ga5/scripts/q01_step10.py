import json

with open('/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json') as f:
    kb = json.load(f)

for i, passage in enumerate(kb[:5]):
    print(f"[{i}]: {passage}")
