// Método que cambia el elemento activo en el menú de los
// usuarios para que coincida con la página actual
document.addEventListener("DOMContentLoaded", function () {
  if (pag_actual) {
    let pag = document.getElementById(pag_actual);
    pag.classList.add("active");
  }
});

// Muestra y oculta la versión móvil del menú de usuario
function toggleMenuUsuario() {
  let menu = document.getElementById("menu-usuario-ul");
  if (menu.classList.contains("show")) {
    menu.classList.remove("show");
  } else {
    menu.classList.add("show");
  }
}
