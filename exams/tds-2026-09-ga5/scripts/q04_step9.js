// Let's find the check button for Question 4 and click it
const buttons = Array.from(document.querySelectorAll('button'));
const q4Btn = buttons.find(b => b.getAttribute('data-question') === 'q-harness-safety-router-server' || b.textContent.includes('Check') && b.closest('div')?.textContent?.includes('Harness'));
if (q4Btn) {
  q4Btn.click();
  return "Clicked Q4 Check button";
}
return "Q4 Check button not found via data-question, let's list all buttons: " + buttons.map(b => b.textContent.trim()).join(' | ');
