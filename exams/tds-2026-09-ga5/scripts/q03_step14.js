// Let's inspect the DOM to find the video element and the button.
const buttons = Array.from(document.querySelectorAll('button'));
const makeVideoBtn = buttons.find(b => b.innerText.includes('Make my video'));
if (makeVideoBtn) {
    makeVideoBtn.click();
    console.log("Clicked Make my video");
} else {
    console.log("Button not found");
}
