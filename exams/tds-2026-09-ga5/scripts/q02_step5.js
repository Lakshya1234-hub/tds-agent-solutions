for (const el of document.querySelectorAll('*')) {
  if (el.textContent.includes('Starter Python script')) {
    let p = el.closest('details');
    if (p) return p.querySelector('code').innerText;
  }
}
return "Not found";
