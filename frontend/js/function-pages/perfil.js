// Obtener el ID del usuario del almacenamiento local
const userId = localStorage.getItem('userId');

if (userId) {
    // Cargar la información del personal de salud
    fetch('http://localhost:3000/personal_salud')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el archivo JSON');
            }
            return response.json();
        })
        .then(data => {
            const user = data.find(user => user.id === userId);
            if (user) {
                // Llenar la información del perfil
                document.querySelector('.nombre').textContent = user.nombre;
                document.querySelector('.rol').textContent = user.rol;
                // Agregar más campos según sea necesario
            } else {
                console.error('Usuario no encontrado');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

    // Cargar el historial de aplicaciones
    fetch('http://localhost:3000/aplicaciones')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el historial de aplicaciones');
            }
            return response.json();
        })
        .then(data => {
            const historial = data.filter(app => app.id_personal === userId);
            const historialTableBody = document.querySelector('.historial tbody');
            historial.forEach(app => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${app.fecha_aplicacion}</td>
                    <td>${app.id_vacuna}</td>
                    <td>${app.dosis}</td>
                    <td>${app.dni_paciente}</td>
                `;
                historialTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
} else {
    console.error('No hay usuario logueado');
}