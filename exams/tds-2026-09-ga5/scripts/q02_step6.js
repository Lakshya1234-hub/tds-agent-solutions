for (const summary of document.querySelectorAll('summary')) {
  if (summary.textContent.includes('Starter Python script')) {
    const parent = summary.parentElement;
    return parent.querySelector('pre code').innerText;
  }
}
return "not found";
