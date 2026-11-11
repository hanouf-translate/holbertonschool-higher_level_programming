document.addEventListener('DOMContentLoaded', (event) => {
    const elementoggle = document.querySelector('#toggle_header');
    const elementheader = document.querySelector('header'); // Fixed selector

    elementoggle.addEventListener('click', function() {
        // Check if the header currently has the 'red' class
        if (elementheader.classList.contains('red')) {
            elementheader.classList.replace('red', 'green');
        } else {
            elementheader.classList.replace('green', 'red');
        }
    });
});