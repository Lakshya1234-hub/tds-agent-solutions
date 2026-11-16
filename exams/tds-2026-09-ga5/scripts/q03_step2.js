// Check for download video link or video element
const links = Array.from(document.querySelectorAll('a'));
const downloadLink = links.find(l => l.textContent.includes('Download video'));
if (downloadLink) {
    return { href: downloadLink.href, text: downloadLink.textContent };
}
const video = document.querySelector('video');
if (video) {
    return { src: video.src };
}
return 'Still waiting or not found';
