// Wait a bit and check video src or blob urls
return new Promise(resolve => {
    setTimeout(() => {
        const video = document.querySelector('video');
        const links = Array.from(document.querySelectorAll('a'));
        const dlLink = links.find(l => l.textContent.includes('Download video'));
        resolve({
            videoSrc: video ? video.src : null,
            videoCurrentSrc: video ? video.currentSrc : null,
            downloadHref: dlLink ? dlLink.href : null
        });
    }, 3000);
});
