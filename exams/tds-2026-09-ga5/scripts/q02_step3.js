const q2 = document.querySelector('[data-question="q-ollama-faiss-rank-correlation-server"]') || document.body;
// find all pre or code or details in question 2
const preTags = Array.from(document.querySelectorAll('pre, code, details'));
return preTags.map(p => p.innerText).filter(t => t.includes('Starter') || t.includes('faiss') || t.includes('spearman') || t.includes('nomic'));
