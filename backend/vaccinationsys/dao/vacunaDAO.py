from .dao_interface import DAOInterface
from vaccinationsys.entities.vacuna import VacunaEntity
from vaccinationsys.models import Vacuna

class VacunaDAO(DAOInterface):
    def crear(self, data: dict) -> VacunaEntity:
        # Create a new Vacuna instance
        vacuna = Vacuna.objects.create(
            dosis_ml=data["dosis_ml"],
            fecha_inyeccion=data["fecha_inyeccion"],
            vial_id=data["vial_id"],
            paciente_id=data["paciente_id"],
            medico_id=data["medico_id"]
        )
        return VacunaEntity(
            id=vacuna.id,
            dosis_ml=vacuna.dosis_ml,
            fecha_inyeccion=vacuna.fecha_inyeccion,
            vial_id=vacuna.vial.id,
            paciente_id=vacuna.paciente.id,
            medico_id=vacuna.medico.id
        )

    def eliminar(self, id: int) -> None:
        # Delete the Vacuna instance by ID
        Vacuna.objects.filter(id=id).delete()

    def modificar(self, id: int, data: dict) -> VacunaEntity:
        # Modify an existing Vacuna instance
        vacuna = Vacuna.objects.get(id=id)
        vacuna.dosis_ml = data["dosis_ml"]
        vacuna.fecha_inyeccion = data["fecha_inyeccion"]
        vacuna.vial_id = data["vial_id"]
        vacuna.paciente_id = data["paciente_id"]
        vacuna.medico_id = data["medico_id"]
        vacuna.save()
        return VacunaEntity(
            id=vacuna.id,
            dosis_ml=vacuna.dosis_ml,
            fecha_inyeccion=vacuna.fecha_inyeccion,
            vial_id=vacuna.vial.id,
            paciente_id=vacuna.paciente.id,
            medico_id=vacuna.medico.id
        )

    def obtener(self, id: int) -> VacunaEntity:
        # Fetch a single Vacuna instance by ID
        vacuna = Vacuna.objects.get(id=id)
        return VacunaEntity(
            id=vacuna.id,
            dosis_ml=vacuna.dosis_ml,
            fecha_inyeccion=vacuna.fecha_inyeccion,
            vial_id=vacuna.vial.id,
            paciente_id=vacuna.paciente.id,
            medico_id=vacuna.medico.id
        )

    def obtenerTodos(self) -> list[VacunaEntity]:
        # Fetch all Vacuna instances
        vacunas = Vacuna.objects.all()
        return [
            VacunaEntity(
                id=vacuna.id,
                dosis_ml=vacuna.dosis_ml,
                fecha_inyeccion=vacuna.fecha_inyeccion,
                vial_id=vacuna.vial.id,
                paciente_id=vacuna.paciente.id,
                medico_id=vacuna.medico.id
            ) for vacuna in vacunas
        ]
