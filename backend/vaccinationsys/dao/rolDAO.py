from .dao_interface import DAOInterface
from vaccinationsys.entities.rol import RolEntity
from vaccinationsys.models import Rol

class RolDAO(DAOInterface):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def crear(self, data: dict) -> RolEntity:
        # Create a new Rol instance
        rol = Rol.objects.create(nombre=data["nombre"])
        return RolEntity(id=rol.id, nombre=rol.nombre)

    def eliminar(self, id: int) -> None:
        # Delete the Rol instance by ID
        Rol.objects.filter(id=id).delete()

    def modificar(self, id: int, data: dict) -> RolEntity:
        # Modify an existing Rol instance
        rol = Rol.objects.get(id=id)
        rol.nombre = data["nombre"]
        rol.save()
        return RolEntity(id=rol.id, nombre=rol.nombre)

    def obtener(self, id: int) -> RolEntity:
        # Fetch a single Rol instance by ID
        rol = Rol.objects.get(id=id)
        return RolEntity(id=rol.id, nombre=rol.nombre)

    def obtenerTodos(self) -> list[RolEntity]:
        # Fetch all Rol instances
        roles = Rol.objects.all()
        return [RolEntity(id=rol.id, nombre=rol.nombre) for rol in roles]
