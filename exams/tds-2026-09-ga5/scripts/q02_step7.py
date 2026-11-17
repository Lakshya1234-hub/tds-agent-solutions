import json
import numpy as np
import faiss
from scipy.stats import spearmanr
import requests

# Load the provided dataset
with open("/home/lakshyadeep/tds-agent/workspace/downloads/q2_dataset.json") as f:
    data = json.load(f)

sentences = data["sentences"]
queries = data["queries"]

# Function to get embeddings from local Ollama
def get_embeddings(model_name, text_list):
    embs = []
    for text in text_list:
        res = requests.post("http://localhost:11434/api/embeddings", json={
            "model": model_name,
            "prompt": text
        }).json()
        embs.append(res["embedding"])
    arr = np.array(embs, dtype=np.float32)
    faiss.normalize_L2(arr)
    return arr

# Embed corpus with both models
emb_a = get_embeddings("nomic-embed-text", sentences)
emb_b = get_embeddings("mxbai-embed-large", sentences)

# Build FAISS indices
index_a = faiss.IndexFlatIP(emb_a.shape[1])
index_a.add(emb_a)
index_b = faiss.IndexFlatIP(emb_b.shape[1])
index_b.add(emb_b)

# Embed queries
emb_q_a = get_embeddings("nomic-embed-text", queries)
emb_q_b = get_embeddings("mxbai-embed-large", queries)

# Calculate matrix
matrix = []
for q in range(len(queries)):
    q_vec_a = emb_q_a[q : q + 1]
    q_vec_b = emb_q_b[q : q + 1]

    D_a, I_a = index_a.search(q_vec_a, 50)
    D_b, I_b = index_b.search(q_vec_b, 50)

    # Top-3 indices
    top3_a = I_a[0][:3].tolist()
    top3_b = I_b[0][:3].tolist()

    # Reconstruct similarity scores array
    scores_a = np.zeros(50)
    scores_b = np.zeros(50)
    scores_a[I_a[0]] = D_a[0]
    scores_b[I_b[0]] = D_b[0]

    # Calculate Spearman correlation
    rho, _ = spearmanr(scores_a, scores_b)
    matrix.append([top3_a[0], top3_a[1], top3_a[2], top3_b[0], top3_b[1], top3_b[2], round(float(rho), 4)])

print(json.dumps(matrix))
