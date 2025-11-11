// Add a click event listener to the element with id "update_header"
document.querySelector('#update_header').addEventListener('click', () => {
  document.querySelector('header').textContent = 'New Header!!!';
});
