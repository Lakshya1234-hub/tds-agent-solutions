// Let's inspect the textarea or input for question 1, and any associated run/check buttons
const textarea = document.querySelector('textarea');
return {
    textareaValue: textarea ? textarea.value : null,
    buttons: Array.from(document.querySelectorAll('button')).map(b => b.textContent.trim())
};
