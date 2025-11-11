// Ensure the DOM is fully loaded before manipulating it
document.addEventListener('DOMContentLoaded', () => {
  // Fetch the translation of "Hello" from the HelloSalut API
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json()) // Parse JSON response
    .then(data => {
      document.querySelector('#hello').textContent = data.hello; // Display the translated "hello"
    })
    .catch(error => console.error('Error fetching translation:', error));
});
