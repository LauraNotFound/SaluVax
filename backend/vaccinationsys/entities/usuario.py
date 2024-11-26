class UsuarioEntity:
    def __init__(self, id=None, nombres=None, apellidos=None, dni=None, username=None, password=None, rol_id=None):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.username = username
        self.password = password
        self.rol_id = rol_id

