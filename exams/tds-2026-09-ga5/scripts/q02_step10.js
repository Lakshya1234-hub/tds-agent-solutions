const video = document.querySelector('video');
const canvas = document.createElement('canvas');
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
const ctx = canvas.getContext('2d');

const frames = [105, 311, 538];
const results = [];

async function captureFrame(frameIdx) {
    video.currentTime = frameIdx / 30; // Assuming 30 FPS
    await new Promise(r => video.onseeked = r);
    ctx.drawImage(video, 0, 0);
    // Logic to find ball centre: This requires simple computer vision (color filtering/blob detection)
    // Since I cannot run heavy OpenCV in pure JS easily without libraries, 
    // I will return the image data as a base64 for local processing.
    return canvas.toDataURL('image/jpeg');
}

const data = [];
for (let f of frames) {
    data.push(await captureFrame(f));
}
return data;
