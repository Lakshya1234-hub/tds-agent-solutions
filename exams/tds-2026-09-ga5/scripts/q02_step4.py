import ollama
import os

model_a_path = "/home/lakshyadeep/ollama/nomic-embed-text"
model_b_path = "/home/lakshyadeep/ollama/mxbai-embed-large"

if not os.path.exists(model_a_path):
    ollama.pull("nomic-embed-text")
if not os.path.exists(model_b_path):
    ollama.pull("mxbai-embed-large")
