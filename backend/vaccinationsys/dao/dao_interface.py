from abc import ABC, abstractmethod
from typing import List

class DAOInterface(ABC):
    @abstractmethod
    def crear(self, data: dict) -> object:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def modificar(self, id: int, data: dict) -> object:
        pass

    @abstractmethod
    def obtener(self, id: int) -> object:
        pass
    
    @abstractmethod
    def obtenerTodos(self) -> List[object]:
        pass
