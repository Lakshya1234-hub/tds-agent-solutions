// Let's check all video sources or blob URLs on the page or console
const videos = document.querySelectorAll('video');
let res = [];
videos.forEach(v => res.push(v.src));
const a = document.querySelector('a[download], a:has-text("Download")');
return {
    videoSrcs: res,
    downloadHref: a ? a.href : null,
    downloadOuter: a ? a.outerHTML : null
};
