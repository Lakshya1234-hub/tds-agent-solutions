import json
import os

kb_path = "/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json"
print("Checking KB path:", kb_path)
if os.path.exists(kb_path):
    with open(kb_path) as f:
        data = json.load(f)
    print(f"Loaded KB with {len(data) if isinstance(data, list) else data.keys()} items.")
else:
    print("KB file not found!")
