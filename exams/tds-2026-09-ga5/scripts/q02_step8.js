const details = Array.from(document.querySelectorAll('details'));
return details.map(d => ({
  summary: d.querySelector('summary')?.innerText,
  text: d.innerText.slice(0, 300)
}));
