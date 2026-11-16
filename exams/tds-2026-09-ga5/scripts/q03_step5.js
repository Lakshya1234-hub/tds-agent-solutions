// Click Make my video if present
const btns = Array.from(document.querySelectorAll('button'));
const makeBtn = btns.find(b => b.textContent.includes('Make my video'));
if (makeBtn) makeBtn.click();

// Also click Download video just in case
const links = Array.from(document.querySelectorAll('a'));
const dlLink = links.find(l => l.textContent.includes('Download video'));
if (dlLink) dlLink.click();

return 'Clicked buttons/links';
