import ollama
if not ollama.is_installed("nomic-embed-text"):
    ollama.pull("nomic-embed-text")
if not ollama.is_installed("mxbai-embed-large"):
    ollama.pull("mxbai-embed-large")
