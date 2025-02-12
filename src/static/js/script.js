const dropdown = document.querySelector('.dropdown');
const button = document.querySelector('.dropdown-button');

button.addEventListener('click', () => {
  dropdown.classList.toggle('active');
});

console.log(123)