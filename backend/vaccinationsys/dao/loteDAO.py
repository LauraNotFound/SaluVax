from vaccinationsys.dao.dao_interface import DAOInterface
from vaccinationsys.entities.lote import LoteEntity
# from .models import Lote
from vaccinationsys.models import Lote

class LoteDAO(DAOInterface):
    def crear(self, data: dict) -> LoteEntity:
        lote = Lote.objects.create(nombre=data["nombre"])
        return LoteEntity(id=lote.id, nombre=lote.nombre)

    def eliminar(self, id: int) -> None:
        Lote.objects.filter(id=id).delete()

    def modificar(self, id: int, data: dict) -> LoteEntity:
        lote = Lote.objects.get(id=id)
        lote.nombre = data.get("nombre", lote.nombre)
        lote.save()
        return LoteEntity(id=lote.id, nombre=lote.nombre)

    def obtener(self, id: int) -> LoteEntity:
        lote = Lote.objects.get(id=id)
        return LoteEntity(id=lote.id, nombre=lote.nombre)
    
    def obtenerTodos(self) -> list:
        lotes = Lote.objects.all()
        return [LoteEntity(id=lote.id, nombre=lote.nombre) for lote in lotes]

