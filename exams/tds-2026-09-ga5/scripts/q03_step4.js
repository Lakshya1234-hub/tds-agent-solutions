const video = document.querySelector('video');
const a = Array.from(document.querySelectorAll('a')).find(el => el.textContent.includes('Download video'));
return {
    videoSrc: video ? video.src : null,
    downloadHref: a ? a.href : null,
    downloadClickable: a ? true : false
};
