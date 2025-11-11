// Add a click event listener to the element with id "add_item"
document.querySelector('#add_item').addEventListener('click', () => {
  const newItem = document.createElement('li'); // Create a new <li> element
  newItem.textContent = 'Item'; // Set its text to "Item"
  document.querySelector('.my_list').appendChild(newItem); // Add it to the <ul> with class "my_list"
});
