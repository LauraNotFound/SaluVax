function cargarAplicaciones() {
    fetch('http://localhost:3000/aplicaciones')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el historial de aplicaciones');
            }
            return response.json();
        })
        .then(data => {
            mostrarAplicaciones(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function mostrarAplicaciones(aplicaciones) {
    const tablaBody = document.getElementById('tabla-aplicaciones');
    tablaBody.innerHTML = ''; 

    aplicaciones.forEach(app => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${app.id_aplicacion}</td>
            <td>${app.nombre_medicamento}</td>
            <td>${app.dosis}</td>
            <td>${app.fecha_aplicacion}</td>
            <td>${app.nombre_paciente}</td>
            <td>${app.nombre_personal}</td>
        `;
        tablaBody.appendChild(row);
    });
}

function busqueda() {
    const input = document.getElementById('busqueda').value.toLowerCase();
    const filas = document.querySelectorAll('#tabla-aplicaciones tr');

    filas.forEach(fila => {
        const textoFila = fila.innerText.toLowerCase();
        fila.style.display = textoFila.includes(input) ? '' : 'none';
    });
}

document.addEventListener('DOMContentLoaded', cargarAplicaciones);
