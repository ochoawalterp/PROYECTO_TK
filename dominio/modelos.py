#Modelo para manejo
from sqlalchemy import Column
from sqlalchemy import String, Integer, Integer
from sqlalchemy.orm import declarative_base

#SE INSTANCIA DE DECLARATIVE BASE
Base = declarative_base()

#SE CREA CLASE QUE HEREDA DE BASE
class TareaModel(Base):

    __tablename__ = "tarea"
    id = Column(Integer, primary_key =True, autoincrement = True)
    nombre  = Column(String(150))
    dia  = Column(Integer)

    #Metodos para retornar valores de tipo string
    def __repr__(self):
        return f'tarea({self.id}, {self.nombre} ,{self.dia})'
    
    def __str__(self):
        return f'tarea({self.id}, {self.nombre} ,{self.dia})'
    
