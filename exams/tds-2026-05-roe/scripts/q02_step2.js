return new Promise((resolve) => {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      resolve(document.querySelectorAll('input[type="email"]').map(input => input.value).join(', '));
    });
  } else {
    resolve(document.querySelectorAll('input[type="email"]').map(input => input.value).join(', '));
  }
});
