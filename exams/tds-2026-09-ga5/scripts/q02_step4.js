const elements = Array.from(document.querySelectorAll('*'));
for (const el of elements) {
  if (el.textContent.includes('Starter Python script') && el.children.length === 0) {
    let parent = el.parentElement;
    while (parent && parent !== document.body) {
      if (parent.tagName === 'DETAILS' || parent.querySelector('pre') || parent.querySelector('code')) {
        return parent.innerHTML;
      }
      parent = parent.parentElement;
    }
  }
}
return "Not found";
