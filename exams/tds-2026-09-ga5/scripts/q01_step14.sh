python3 -c "
import json
with open('/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json') as f:
    data = json.load(f)
print(type(data), len(data) if isinstance(data, list) else list(data.keys()))
if isinstance(data, list) and len(data) > 0:
    print(data[0])
"
