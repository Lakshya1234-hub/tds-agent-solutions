// Let's check what elements or attributes or handlers are associated with Q1 'Run 20-Probe Gauntlet' or similar buttons
const buttons = Array.from(document.querySelectorAll('button'));
const q1Button = buttons.find(b => b.textContent.includes('Run 20-Probe Gauntlet'));
return {
    buttonHtml: q1Button ? q1Button.outerHTML : null,
    listeners: q1Button ? q1Button.onclick : null
};
