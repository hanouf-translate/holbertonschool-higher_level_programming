document.addEventListener('DOMContentLoaded',(event)=> {
    const lementheader = document.querySelector('#update_header');
    const elementheader = document.querySelector('header');
    lementheader.addEventListener('click', function() {
        elementheader.textContent= 'New Header!!!';
    });
});