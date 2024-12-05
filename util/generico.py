import os


def crear_carpeta_si_no_existe(ruta, nombre_carperta):
    ruta_completa = os.path.join(ruta,nombre_carperta)
#aca guardariamos nuestra base de datos para eso se crea la carpeta
    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
        return True, f' Se ha creado la carpeta {nombre_carperta} en {ruta}'
    else:
        return False, f"La carpeta '{nombre_carperta}' ya existen en ruta '{ruta}'"

