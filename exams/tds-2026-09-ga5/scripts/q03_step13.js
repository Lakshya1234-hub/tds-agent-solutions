// Make the video first by clicking the button
document.querySelector('button[data-question="q-ball-tracker-server"]').click();

// Wait a bit for the video to generate, then get the download link
setTimeout(() => {
  const downloadLink = document.querySelector('a[href*="blob:"]');
  if (downloadLink) {
    console.log(downloadLink.href);
  } else {
    console.log("No download link found");
  }
}, 5000);
