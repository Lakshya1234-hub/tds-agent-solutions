// Check if a video element or link appeared
const video = document.querySelector('video');
if (video) {
    return video.src;
}
return "No video element found yet. Waiting...";
