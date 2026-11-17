// Let's check exam-tds-2026-09-ga5.js or related scripts in the page
const scripts = Array.from(document.querySelectorAll('script')).map(s => s.src);
return scripts;
