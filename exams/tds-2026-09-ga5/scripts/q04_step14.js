// Let's inspect window object properties or evaluate how the page makes requests
return Object.keys(window).filter(k => k.includes('Sign') || k.includes('email') || k.includes('quiz'));
