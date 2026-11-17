// Let's click the "Run 20-Probe Gauntlet" button or interact with the page
const btn = Array.from(document.querySelectorAll('button')).find(el => el.textContent.includes('Run 20-Probe Gauntlet'));
if (btn) {
    btn.click();
    return "Clicked Run 20-Probe Gauntlet";
}
return "Button not found";
