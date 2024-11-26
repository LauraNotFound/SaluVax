from vaccinationsys.dao.dao_interface import DAOInterface
from vaccinationsys.entities.paciente import PacienteEntity
from vaccinationsys.models import Paciente

class PacienteDAO(DAOInterface):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def crear(self, data: dict) -> PacienteEntity:
        paciente = Paciente.objects.create(
            nombres=data["nombres"],
            apellidos=data["apellidos"],
            dni=data["dni"],
            direccion=data["direccion"],
            celular=data["celular"],
            fecha_nacimiento=data["fecha_nacimiento"]
        )
        return PacienteEntity(
            id=paciente.id,
            nombres=paciente.nombres,
            apellidos=paciente.apellidos,
            dni=paciente.dni,
            direccion=paciente.direccion,
            celular=paciente.celular,
            fecha_nacimiento=paciente.fecha_nacimiento
        )

    def eliminar(self, id: int) -> None:
        Paciente.objects.filter(id=id).delete()

    def modificar(self, id: int, data: dict) -> PacienteEntity:
        paciente = Paciente.objects.get(id=id)
        paciente.nombres = data.get("nombres", paciente.nombres)
        paciente.apellidos = data.get("apellidos", paciente.apellidos)
        paciente.dni = data.get("dni", paciente.dni)
        paciente.direccion = data.get("direccion", paciente.direccion)
        paciente.celular = data.get("celular", paciente.celular)
        paciente.fecha_nacimiento = data.get("fecha_nacimiento", paciente.fecha_nacimiento)
        paciente.save()
        return PacienteEntity(
            id=paciente.id,
            nombres=paciente.nombres,
            apellidos=paciente.apellidos,
            dni=paciente.dni,
            direccion=paciente.direccion,
            celular=paciente.celular,
            fecha_nacimiento=paciente.fecha_nacimiento
        )

    def obtener(self, id: int) -> PacienteEntity:
        paciente = Paciente.objects.get(id=id)
        return PacienteEntity(
            id=paciente.id,
            nombres=paciente.nombres,
            apellidos=paciente.apellidos,
            dni=paciente.dni,
            direccion=paciente.direccion,
            celular=paciente.celular,
            fecha_nacimiento=paciente.fecha_nacimiento
        )
    
    def obtenerTodos(self) -> list:
        pacientes = Paciente.objects.all()
        return [PacienteEntity(
            id=paciente.id,
            nombres=paciente.nombres,
            apellidos=paciente.apellidos,
            dni=paciente.dni,
            direccion=paciente.direccion,
            celular=paciente.celular,
            fecha_nacimiento=paciente.fecha_nacimiento
        ) for paciente in pacientes]
