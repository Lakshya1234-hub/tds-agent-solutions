// Click the Make my video button
const btn = document.querySelector('button[data-question="q-ollama-faiss-rank-correlation-server"]');
// Wait, the question text changed in the portal but the ID was the same? 
// Let me look for buttons to generate a video for the new "red ball" question.
const videoBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Make my video'));
if (videoBtn) {
    videoBtn.click();
    return "Clicked";
}
return "Button not found";
