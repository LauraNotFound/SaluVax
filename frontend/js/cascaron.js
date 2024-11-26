function openTab(evt, tabName) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  const tab = document.getElementById(tabName);
  tab.style.display = "block";

  if (tabName === "CerrarSesion") {
    window.location.href = "/html/inicio-sesion.html";
    return;
  }

  loadTabContent(tabName);

  evt.currentTarget.className += " active";
}

function loadTabContent(tabName) {
  const contentMap = {
    "Perfil": "/html/pages/perfil.html",
    "StockVacunas": "/html/pages/stock-vacunas.html",
    "RegistroAplicaciones": "/html/pages/registro-aplicaciones.html",
    "AplicacionVacuna": "/html/pages/aplicacion-vacuna.html"
  };

  const filePath = contentMap[tabName];
  const container = document.querySelector(`#${tabName} div`);

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

        if (tabName === "RegistroAplicaciones") {
          cargarAplicaciones();
        }
        if (tabName === "StockVacunas") {
          cargarVacunas();
        }
        if (tabName === "Perfil") {
          cargarHistorialAplicacionesPersonal();
        }
      })
      .catch(error => {
        container.innerHTML = `<p>Error al cargar el contenido: ${error.message}</p>`;
      });
  }
}

document.getElementById("defaultOpen").click();
