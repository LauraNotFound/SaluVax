from abc import ABC, abstractmethod

class DAOInterface(ABC):
    @abstractmethod
    def crear(self, data):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass

    @abstractmethod
    def modificar(self, id, data):
        pass

    @abstractmethod
    def obtener(self, id):
        pass
    
    @abstractmethod
    def obtenerTodos(self, data):
        pass
