const pres = Array.from(document.querySelectorAll('pre'));
return pres.map(p => p.textContent).join('\n---\n');
