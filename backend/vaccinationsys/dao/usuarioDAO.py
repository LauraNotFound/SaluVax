from .dao_interface import DAOInterface
from vaccinationsys.entities.usuario import UsuarioEntity
from vaccinationsys.models import Usuario

class UsuarioDAO(DAOInterface):
    def crear(self, data: dict) -> UsuarioEntity:
        # Create a new Usuario instance
        usuario = Usuario.objects.create(
            nombres=data["nombres"],
            apellidos=data["apellidos"],
            dni=data["dni"],
            username=data["username"],
            password=data["password"],
            rol_id=data["rol_id"]
        )
        return UsuarioEntity(
            id=usuario.id,
            nombres=usuario.nombres,
            apellidos=usuario.apellidos,
            dni=usuario.dni,
            username=usuario.username,
            password=usuario.password,
            rol_id=usuario.rol.id
        )

    def eliminar(self, id: int) -> None:
        # Delete the Usuario instance by ID
        Usuario.objects.filter(id=id).delete()

    def modificar(self, id: int, data: dict) -> UsuarioEntity:
        # Modify an existing Usuario instance
        usuario = Usuario.objects.get(id=id)
        usuario.nombres = data["nombres"]
        usuario.apellidos = data["apellidos"]
        usuario.dni = data["dni"]
        usuario.username = data["username"]
        usuario.password = data["password"]
        usuario.rol_id = data["rol_id"]
        usuario.save()
        return UsuarioEntity(
            id=usuario.id,
            nombres=usuario.nombres,
            apellidos=usuario.apellidos,
            dni=usuario.dni,
            username=usuario.username,
            password=usuario.password,
            rol_id=usuario.rol.id
        )

    def obtener(self, id: int) -> UsuarioEntity:
        # Fetch a single Usuario instance by ID
        usuario = Usuario.objects.get(id=id)
        return UsuarioEntity(
            id=usuario.id,
            nombres=usuario.nombres,
            apellidos=usuario.apellidos,
            dni=usuario.dni,
            username=usuario.username,
            password=usuario.password,
            rol_id=usuario.rol.id
        )

    def obtenerTodos(self) -> list[UsuarioEntity]:
        # Fetch all Usuario instances
        usuarios = Usuario.objects.all()
        return [
            UsuarioEntity(
                id=usuario.id,
                nombres=usuario.nombres,
                apellidos=usuario.apellidos,
                dni=usuario.dni,
                username=usuario.username,
                password=usuario.password,
                rol_id=usuario.rol.id
            ) for usuario in usuarios
        ]
