// Obtener referencias al ícono hamburguesa y al menú
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

// Función para alternar el menú al hacer clic en el ícono hamburguesa
hamburger.addEventListener('click', (event) => {
    navLinks.classList.toggle('active');
    event.stopPropagation(); // Evitar que el clic en el ícono cierre el menú
});

// Función para cerrar el menú si se hace clic fuera de él
document.addEventListener('click', (event) => {
    // Verificar si el menú está abierto y si el clic ocurrió fuera del menú y el ícono hamburguesa
    const isClickInsideMenu = navLinks.contains(event.target);
    const isClickOnHamburger = hamburger.contains(event.target);
    
    // Si el clic no es en el menú ni en el ícono, cerramos el menú
    if (!isClickInsideMenu && !isClickOnHamburger) {
        navLinks.classList.remove('active');
    }
});

// scripts.js
window.onscroll = function() {fixNavbar()};

// Obtener la barra de navegación
var menu = document.getElementById("menu");
var etiqueta = document.getElementById("etiqueta");
var etiqueta1 = document.getElementById("etiqueta1");
var etiqueta2 = document.getElementById("etiqueta2");
var etiqueta3 = document.getElementById("etiqueta3");
var etiqueta4 = document.getElementById("etiqueta4");
var etiqueta5 = document.getElementById("etiqueta5");
// Obtener la posición original de la barra de navegación
var sticky = menu.offsetTop;

function fixNavbar() {
  // Si la posición del scroll es mayor o igual que la posición de la barra de navegación
  if (window.scrollY >= sticky) {
    menu.classList.add("fixed");
    etiqueta.classList.add("fijo");
    etiqueta1.classList.add("fijo");
    etiqueta2.classList.add("fijo");
    etiqueta3.classList.add("fijo");
    etiqueta4.classList.add("fijo");
    etiqueta5.classList.add("fijo");

  } else {
    menu.classList.remove("fixed");
    etiqueta.classList.remove("fijo");
    etiqueta1.classList.remove("fijo");
    etiqueta2.classList.remove("fijo");
    etiqueta3.classList.remove("fijo");
    etiqueta4.classList.remove("fijo");
    etiqueta5.classList.remove("fijo");
  }
}

