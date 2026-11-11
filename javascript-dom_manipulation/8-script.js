fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => {
        if(!response.ok){
            throw new Error(`HTTP error: ${response.status}`); 
        } return response.json();
    })
    .then(data => {
        const elementhello = document.querySelector('#hello');
        elementhello.textContent= data.hello;

    })