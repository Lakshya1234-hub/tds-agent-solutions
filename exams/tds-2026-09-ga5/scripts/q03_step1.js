async function run() {
    // Find question 3 container and click Make my video
    const btn = document.querySelector('button[data-question="q-ball-tracker-server"]');
    if (!btn) return "Button not found";
    // Let's find the 'Make my video' button inside or nearby
    const makeBtn = Array.from(document.querySelectorAll('button')).b => b.textContent.includes('Make my video') ? b : null; // wait, syntax fix
    const buttons = Array.from(document.querySelectorAll('button'));
    let targetBtn = buttons.find(b => b.textContent.includes('Make my video'));
    if (targetBtn) targetBtn.click();
    
    // Wait for video element or download button
    await new Promise(r => setTimeout(r, 4000));
    
    let downloadA = Array.from(document.querySelectorAll('a')).find(a => a.textContent.includes('Download video'));
    if (!downloadA || !downloadA.href) return "Download video link not ready";
    
    let resp = await fetch(downloadA.href);
    let blob = await resp.blob();
    return new Promise((resolve) => {
        let reader = new FileReader();
        reader.onload = () => resolve({ "__save_file__": "ball_video.webm", "__base64__": reader.result.split(',')[1] });
        reader.readAsDataURL(blob);
    });
}
return run();
