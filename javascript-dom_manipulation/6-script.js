fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((response) => {
        if(!response.ok){
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
        })
    .then(data => {
    const name = document.querySelector('#character');
    name.textContent = data.name;  
    })
 