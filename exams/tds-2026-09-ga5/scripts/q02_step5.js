// List all elements to find the video or download button
const buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText);
const links = Array.from(document.querySelectorAll('a')).map(a => a.href);
const video = document.querySelector('video');
return { buttons, links, hasVideo: !!video };
