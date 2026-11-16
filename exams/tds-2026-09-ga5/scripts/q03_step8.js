return new Promise(resolve => {
    setTimeout(async () => {
        const video = document.getElementById('q-ball-tracker-server-video');
        const status = document.getElementById('q-ball-tracker-server-status');
        const download = document.getElementById('q-ball-tracker-server-download');
        
        // If video has src or blob
        let src = video ? video.src : null;
        let videoBlobUrl = null;
        if (video && video.src) {
            // fetch blob
            const resp = await fetch(video.src);
            const blob = await resp.blob();
            const buffer = await blob.arrayBuffer();
            // We can save it via python or base64
            const base64 = btoa(String.fromCharCode(...new Uint8Array(buffer)));
            videoBlobUrl = base64;
        }
        
        resolve({
            statusText: status ? status.textContent : null,
            videoSrc: src,
            downloadHref: download ? download.href : null,
            videoBlobBase64: videoBlobUrl ? videoBlobUrl.slice(0, 50) + '...' : null
        });
    }, 6000);
});
