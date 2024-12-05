import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelos import TareaModel
from typing import List  # Asegúrate de importar List de typing
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class ServicioTarea():
    

    def __init__(self):
        self.engine = db.create_engine('sqlite:///bd/todoapp.sqlite', echo = True , future= True)
    
    def registro(self, nombre, dia):
        tarea = TareaModel()
        tarea.nombre = nombre
        tarea.dia =dia

        with Session(self.engine) as session:
            session.add(tarea)
            session.commit()


    def modificar(self,nombre,dia,tarea_id):

        try:
            #Buscar la tarea en la base de datos
            with Session(self.engine) as session:
                tarea = session.query(TareaModel).filter_by(id=tarea_id).one()

                #Actualizar los atributos de la tarea
                tarea.nombre = nombre
                tarea.dia = dia

                #Confirmamos los cambios en la base de datos
                session.commit()
                print(f'Tarea con ID {tarea_id} Actualizada correctamente')

        except NoResultFound:
            print(f'No se encontroningún producto con ID {tarea_id}. No se realizo ninguna modificacion')
            return False
        except Exception as e:
            print(f"Error al actualizar la tarea: {e}")
            return False
        

    def obtener_tareas(self)-> List[TareaModel]:
        tareas: TareaModel = None
        with Session(self.engine)as session:
            tareas = session.query(TareaModel).all() 
            return tareas

    def eliminar_tareas(self, tarea_id):

        with Session(self.engine) as session:
            tarea = session.query(TareaModel).filter_by(id =tarea_id).first()
            if tarea:
                try:
                    session.delete(tarea)
                    session.commit()
                    print(f"La tarea con ID{tarea_id} fue eliminada correctamente")

                except IntegrityError as e:
                    session.rollback()
                    print(f"No se puede eliminar la tarea ID{tarea_id}. Error: {e}")
            else:
                print(f"No se encontro ninguna Tarea con ID {tarea_id}")