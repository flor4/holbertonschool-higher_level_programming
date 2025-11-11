// Fetch character data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    document.querySelector('#character').textContent = data.name; // Display the character name
  })
  .catch(error => console.error('Error fetching character:', error));
