document.addEventListener('DOMContentLoaded' ,(event)=> {
    const elementlist = document.querySelector('#add_item');
    const elementlists = document.querySelector('.my_list');
    elementlist.addEventListener('click', function() {
        elementlists.innerHTML += "<li>Item</li>";
    });
});