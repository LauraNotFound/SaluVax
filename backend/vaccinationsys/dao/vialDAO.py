from vaccinationsys.dao.dao_interface import DAOInterface
from vaccinationsys.entities.vial import VialEntity
from vaccinationsys.models import Vial

class VialDAO(DAOInterface):
    def crear(self, data: dict) -> VialEntity:
        vial = Vial.objects.create(
            nombre=data["nombre"],
            kit=data["kit"],
            enfermedad=data["enfermedad"],
            fecha_caducidad=data["fecha_caducidad"],
            lote_id=data["lote_id"]
        )
        return VialEntity(
            id=vial.id,
            nombre=vial.nombre,
            kit=vial.kit,
            enfermedad=vial.enfermedad,
            fecha_caducidad=vial.fecha_caducidad,
            lote_id=vial.lote_id
        )

    def eliminar(self, id: int) -> None:
        Vial.objects.filter(id=id).delete()

    def modificar(self, id: int, data: dict) -> VialEntity:
        vial = Vial.objects.get(id=id)
        vial.nombre = data.get("nombre", vial.nombre)
        vial.kit = data.get("kit", vial.kit)
        vial.enfermedad = data.get("enfermedad", vial.enfermedad)
        vial.fecha_caducidad = data.get("fecha_caducidad", vial.fecha_caducidad)
        vial.lote_id = data.get("lote_id", vial.lote_id)
        vial.save()
        return VialEntity(
            id=vial.id,
            nombre=vial.nombre,
            kit=vial.kit,
            enfermedad=vial.enfermedad,
            fecha_caducidad=vial.fecha_caducidad,
            lote_id=vial.lote_id
        )

    def obtener(self, id: int) -> VialEntity:
        vial = Vial.objects.get(id=id)
        return VialEntity(
            id=vial.id,
            nombre=vial.nombre,
            kit=vial.kit,
            enfermedad=vial.enfermedad,
            fecha_caducidad=vial.fecha_caducidad,
            lote_id=vial.lote_id
        )
    
    def obtenerTodos(self) -> list:
        viales = Vial.objects.all()
        return [VialEntity(
            id=vial.id,
            nombre=vial.nombre,
            kit=vial.kit,
            enfermedad=vial.enfermedad,
            fecha_caducidad=vial.fecha_caducidad,
            lote_id=vial.lote_id
        ) for vial in viales]
