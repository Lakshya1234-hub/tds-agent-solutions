import json
import os

kb_path = '/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json'
print("File exists:", os.path.exists(kb_path))
if os.path.exists(kb_path):
    with open(kb_path) as f:
        data = json.load(f)
    print("Type:", type(data))
    print("Length:", len(data) if isinstance(data, (list, dict)) else "N/A")
    if isinstance(data, list) and len(data) > 0:
        print("Sample:", data[0])
