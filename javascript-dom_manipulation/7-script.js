// Fetch all Star Wars films from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse JSON response
  .then(data => {
    const movies = data.results; // Array of film objects
    const list = document.querySelector('#list_movies'); // Select the <ul> element

    // Loop through each movie and create a <li> for its title
    movies.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      list.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error fetching movies:', error));
