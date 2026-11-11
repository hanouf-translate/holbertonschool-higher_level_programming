fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => {
        if(!response.ok){
            throw new Error(`HTTP error: ${response.status}`);   
        }
        return response.json();
    })
    .then(data => {
        const elementlist = document.querySelector('#list_movies');
        data.results.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            elementlist.appendChild(li);
        });

    }) 
    