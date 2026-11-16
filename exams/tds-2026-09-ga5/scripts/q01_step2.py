import json

with open('/home/lakshyadeep/tds-agent/workspace/downloads/q1_knowledge_base.json', 'r') as file:
    knowledge_base = json.load(file)

passages = knowledge_base['passages']
print(passages)
