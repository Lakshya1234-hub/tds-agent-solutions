// Let's click "Make my video" or see what buttons are available
const buttons = Array.from(document.querySelectorAll('button'));
const makeVideoBtn = buttons.find(b => b.textContent.includes('Make my video'));
if (makeVideoBtn) {
    makeVideoBtn.click();
    return 'Clicked Make my video';
}
return 'Button not found';
