#Contruir la base de datos

import sqlalchemy as db #Importar para interactuar con la base de datos
import util.generico as gen #Importamos modulo personalizado para funcinalidades genericas
import dominio.modelos as modelos #Importamos los modelos de la base de datos

#nombre de la carpeta que deseas crear para almancenar la base de datos
nombre_carpeta = "bd"

#Ruta donde se almacenara la base de datos
ruta = "./"

#Crear la carpeta si no existe
gen.crear_carpeta_si_no_existe(ruta, nombre_carpeta)

engine = db.create_engine('sqlite:///bd/todoapp.sqlite', echo = True , future = True)


modelos.Base.metadata.create_all(engine)

# Siempre cierra la conexión después de usarla
connection = engine.connect()
# Realiza operaciones...
connection.close()