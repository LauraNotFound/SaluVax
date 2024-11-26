function openTab(evt, tabName) {
  var i, tabcontent, tablinks;

  // Ocultar todos los elementos con la clase "tabcontent"
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Quitar la clase "active" de todos los botones de las pestañas
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Mostrar el contenido de la pestaña seleccionada
  const tab = document.getElementById(tabName);
  tab.style.display = "block";

  // Verificar si es la pestaña de "Cerrar Sesión"
  if (tabName === "CerrarSesion") {
    window.location.href = "/html/inicio-sesion.html";
    return;
  }

  // Cargar contenido dinámico basado en la pestaña
  loadTabContent(tabName);

  // Agregar la clase "active" al botón seleccionado
  evt.currentTarget.className += " active";
}

// Cargar contenido de cada pestaña desde un archivo HTML externo
function loadTabContent(tabName) {
  const contentMap = {
    "Perfil": "/html/pages/perfil.html",
    "StockVacunas": "/html/pages/stock-vacunas.html",
    "RegistroAplicaciones": "/html/pages/registro-aplicaciones.html",
    "AplicacionVacuna": "/html/pages/aplicacion-vacuna.html"
  };

  // Ruta al archivo HTML correspondiente
  const filePath = contentMap[tabName];
  const container = document.querySelector(`#${tabName} div`);

  // Verificar si el archivo está definido para la pestaña
  if (filePath) {
    fetch(filePath)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error al cargar ${filePath}: ${response.statusText}`);
        }
        return response.text();
      })
      .then(html => {
        container.innerHTML = html;
      })
      .catch(error => {
        container.innerHTML = `<p>Error al cargar el contenido: ${error.message}</p>`;
      });
  }
}

// Abrir la pestaña por defecto al cargar la página
document.getElementById("defaultOpen").click();
