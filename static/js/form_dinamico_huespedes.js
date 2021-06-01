// Permite añadir dinámicamente formularios a un formset.
// Actualmente configurado para funcionar con la lista de huéspedes
// en el formulario de creación de Orden de Compra.


let formHuesped = document.querySelectorAll(".form-huesped");
let container = document.querySelector("#form-huespedes");
let addButton = document.querySelector("#add-form");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formNum = formHuesped.length - 1;
addButton.addEventListener("click", addForm);

function addForm(e) {
  e.preventDefault();

  let newForm = formHuesped[0].cloneNode(true);
  let formRegex = RegExp(`form-(\\d){1}-`, "g");

  formNum++;
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
  container.insertBefore(newForm, addButton);

  totalForms.setAttribute("value", `${formNum + 1}`);
}
