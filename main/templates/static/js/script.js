const menuToggle = document.querySelector('.menu-toggle');
const container = document.querySelector('.container');

menuToggle.addEventListener('click', function() {
    container.classList.toggle('menu-opened');
});