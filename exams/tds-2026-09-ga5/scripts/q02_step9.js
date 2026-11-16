for (const d of document.querySelectorAll('details')) {
  if (d.querySelector('summary')?.innerText.includes('Starter Python script')) {
    return d.innerText;
  }
}
return "not found";
