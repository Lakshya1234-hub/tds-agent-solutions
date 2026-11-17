// Let's scroll down to Question 4 and see its status or check button details
const q4Div = Array.from(document.querySelectorAll('div')).find(d => d.textContent.includes('Harness Engineering'));
if (q4Div) {
  q4Div.scrollIntoView();
  const checkBtn = q4Div.querySelector('button') || document.querySelector('button[data-question="q-harness-safety-router-server"]');
  if (checkBtn) {
    checkBtn.click();
    return "Clicked Q4 button via scrollIntoView";
  }
}
return "Not found";
