import json

with open('dataset.json', 'r') as file:
    data = json.load(file)

sentences = data['sentences']
queries = data['queries']
