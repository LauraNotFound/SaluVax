function cargarVacunas() {
    fetch('http://localhost:3000/vacunas')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el stock de vacunas');
            }
            return response.json();
        })
        .then(data => {
            mostrarVacunas(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function mostrarVacunas(vacunas) {
    const tablaBody = document.getElementById('tabla-vacunas');
    if (!tablaBody) {
        console.error('No se encontró el elemento tabla-vacunas');
        return; 
    }
    tablaBody.innerHTML = ''; 

    vacunas.forEach(vacuna => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${vacuna.id_vacuna}</td>
            <td>${vacuna.nombre}</td>
            <td>${vacuna.lote}</td>
            <td>${vacuna.fecha_caducidad}</td>
            <td>${vacuna.stock}</td>
            <td>${vacuna.descripcion}</td>
        `;
        tablaBody.appendChild(row);
    });
}

function busqueda() {
    const input = document.getElementById('busqueda').value.toLowerCase();
    const filas = document.querySelectorAll('#tabla-vacunas tr');

    filas.forEach(fila => {
        const textoFila = fila.innerText.toLowerCase();
        fila.style.display = textoFila.includes(input) ? '' : 'none';
    });
}

document.addEventListener('DOMContentLoaded', cargarVacunas);