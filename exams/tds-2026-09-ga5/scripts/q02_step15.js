// Find the video element source and extract the blob
const video = document.querySelector('video');
if (video) {
    return video.src;
} else {
    // Look for a link to the video
    const link = document.querySelector('a[href*="mp4"]');
    return link ? link.href : "No video source found";
}
