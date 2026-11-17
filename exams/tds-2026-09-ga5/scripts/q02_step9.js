// Inspect page to find the video for the new question
const videoElement = document.querySelector('video');
if (videoElement) {
    return {
        src: videoElement.src,
        id: videoElement.id
    };
} else {
    return "No video found";
}
