const userId = localStorage.getItem('userId');
console.log('User  ID:', userId);

if (userId) {

    fetch('http://localhost:3000/personal_salud')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el archivo JSON');
            }
            return response.json();
        })
        .then(data => {
            console.log('Datos de personal de salud:', data); 
            const user = data.find(user => user.id === userId);
            if (user) {
                document.querySelector('.nombres').textContent = user.nombre || 'Cargando...';
                document.querySelector('.apellidos').textContent = user.apellido || 'Cargando...';
                document.querySelector('.sexo').textContent = user.sexo || 'Cargando...';
                document.querySelector('.fech-nac').textContent = user.fecha_nacimiento || 'Cargando...';
                document.querySelector('.dni').textContent = user.dni || 'Cargando...';
                document.querySelector('.rol').textContent = user.rol || 'Cargando...';
                document.querySelector('.estado').textContent = user.estado || 'Cargando...';
            } else {
                console.error('Usuario no encontrado');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

    cargarHistorialAplicacionesPersonal();
} else {
    console.error('No hay usuario logueado');
}

function cargarHistorialAplicacionesPersonal() {
    fetch('http://localhost:3000/aplicaciones')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el historial de aplicaciones');
            }
            return response.json();
        })
        .then(data => {
            console.log('Historial de aplicaciones:', data);
            const historial = data.filter(historial => {
                return String(historial.id_personal_salud) === userId;
            });
            console.log('Tipo de userId:', typeof userId);
            console.log('Tipo de id_personal_salud:', typeof historial.id_personal_salud);
            console.log('Historial filtrado:', historial);
            const historialTableBody = document.querySelector('.historial tbody');
            historialTableBody.innerHTML = '';
            historial.forEach(historial => {
                const row = document.createElement('tr');
                row.innerHTML = `
            <td>${historial.fecha_aplicacion}</td>
            <td>${historial.id_vacuna}</td>
            <td>${historial.dosis}</td>
            <td>${historial.nombre_paciente}</td>
        `;
                historialTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        }
    );
}