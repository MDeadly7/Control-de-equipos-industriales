<<<<<<< HEAD
import csv
from datetime import datetime

# Nombre del archivo de equipos
NOMBRE_ARCHIVO = 'equipos.csv'
ENCABEZADOS = ['ID', 'Nombre', 'Tipo', 'ValorCalibracion', 'FechaUltimoMantenimiento']

def crear_archivo_si_no_existe():
    """
    Crea el archivo CSV de equipos con los encabezados si no existe.
    """
    try:
        with open(NOMBRE_ARCHIVO, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(ENCABEZADOS)
        print(f"Archivo '{NOMBRE_ARCHIVO}' creado con éxito.")
    except FileExistsError:
        pass # El archivo ya existe, no hacemos nada
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

def leer_equipos():
    """
    Lee todos los equipos del archivo CSV y devuelve una lista de diccionarios.
    """
    crear_archivo_si_no_existe() # Aseguramos que el archivo exista antes de leer
    equipos = []
    try:
        with open(NOMBRE_ARCHIVO, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                equipos.append(row)
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{NOMBRE_ARCHIVO}' no se encontró. Se creará al agregar equipos.")
    except Exception as e:
        print(f"Error al leer equipos: {e}")
    return equipos

def guardar_equipos(equipos):
    """
    Guarda una lista de equipos (diccionarios) en el archivo CSV.
    """
    try:
        with open(NOMBRE_ARCHIVO, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            writer.writeheader()
            writer.writerows(equipos)
    except Exception as e:
        print(f"Error al guardar equipos: {e}")

# Ejecutamos para asegurar que el archivo existe
crear_archivo_si_no_existe()

print("\n--- Contenido inicial del archivo (después de crear/verificar) ---")
for equipo in leer_equipos():
    print(equipo)
=======
import csv
from datetime import datetime

# Nombre del archivo de equipos
NOMBRE_ARCHIVO = 'equipos.csv'
ENCABEZADOS = ['ID', 'Nombre', 'Tipo', 'ValorCalibracion', 'FechaUltimoMantenimiento']

def crear_archivo_si_no_existe():
    """
    Crea el archivo CSV de equipos con los encabezados si no existe.
    """
    try:
        with open(NOMBRE_ARCHIVO, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(ENCABEZADOS)
        print(f"Archivo '{NOMBRE_ARCHIVO}' creado con éxito.")
    except FileExistsError:
        pass # El archivo ya existe, no hacemos nada
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

def leer_equipos():
    """
    Lee todos los equipos del archivo CSV y devuelve una lista de diccionarios.
    """
    crear_archivo_si_no_existe() # Aseguramos que el archivo exista antes de leer
    equipos = []
    try:
        with open(NOMBRE_ARCHIVO, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                equipos.append(row)
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{NOMBRE_ARCHIVO}' no se encontró. Se creará al agregar equipos.")
    except Exception as e:
        print(f"Error al leer equipos: {e}")
    return equipos

def guardar_equipos(equipos):
    """
    Guarda una lista de equipos (diccionarios) en el archivo CSV.
    """
    try:
        with open(NOMBRE_ARCHIVO, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            writer.writeheader()
            writer.writerows(equipos)
    except Exception as e:
        print(f"Error al guardar equipos: {e}")

# Ejecutamos para asegurar que el archivo existe
crear_archivo_si_no_existe()

print("\n--- Contenido inicial del archivo (después de crear/verificar) ---")
for equipo in leer_equipos():
    print(equipo)
    
#Lectura secuencial
def listar_equipos_secuencial():
    """
    Lee el archivo secuencialmente y muestra todos los detalles de los equipos.
    """
    print("\n--- Listado Secuencial de Equipos ---")
    equipos = leer_equipos()
    if not equipos:
        print("No hay equipos registrados.")
        return

    for equipo in equipos:
        print(f"ID: {equipo.get('ID', 'N/A')}")
        print(f"Nombre: {equipo.get('Nombre', 'N/A')}")
        print(f"Tipo: {equipo.get('Tipo', 'N/A')}")
        print(f"Valor de Calibración: {equipo.get('ValorCalibracion', 'N/A')}")
        print(f"Fecha Último Mantenimiento: {equipo.get('FechaUltimoMantenimiento', 'N/A')}")
        print("-" * 30)

# Ejemplo de uso:
listar_equipos_secuencial()

