document.getElementById('ingresarForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:3000/personal_salud')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el archivo JSON');
            }
            return response.json();
        })
        .then(data => {
            console.log('Respuesta de la API:', data);

            const user = data.find(user => user.usuario === username && user.contrasenia === password);

            if (user) {
                localStorage.setItem('userId', user.id);
                window.location.href = 'cascaron.html';
            } else {
                alert('Usuario o contraseña incorrectos');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ocurrió un error: ' + error.message); 
        });
});