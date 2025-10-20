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

#CRUD

def obtener_siguiente_id():
    """
    Calcula el siguiente ID disponible para un nuevo equipo.
    """
    equipos = leer_equipos()
    if not equipos:
        return 1
    # Convertimos los IDs a enteros y buscamos el máximo, luego le sumamos 1
    max_id = max([int(e['ID']) for e in equipos if e['ID'].isdigit()])
    return max_id + 1

def agregar_equipo():
    """
    Permite al usuario ingresar los datos de un nuevo equipo y lo guarda.
    """
    print("\n--- Agregar Nuevo Equipo ---")
    equipo_id = obtener_siguiente_id()
    print(f"ID del nuevo equipo: {equipo_id}")
    nombre = input("Nombre del equipo: ")
    tipo = input("Tipo de equipo (Ej. 'Sensor', 'Actuador', 'PLC'): ")
    valor_calibracion = input("Valor de calibración (Dejar en blanco si no aplica): ")
    fecha_mantenimiento = input("Fecha del último mantenimiento (YYYY-MM-DD): ")

    nuevo_equipo = {
        'ID': str(equipo_id),
        'Nombre': nombre,
        'Tipo': tipo,
        'ValorCalibracion': valor_calibracion if valor_calibracion else 'NA',
        'FechaUltimoMantenimiento': fecha_mantenimiento
    }

    equipos = leer_equipos()
    equipos.append(nuevo_equipo)
    guardar_equipos(equipos)
    print("Equipo agregado con éxito.")

def modificar_equipo(equipo_id):
    """
    Permite modificar un equipo existente por su ID.
    """
    print(f"\n--- Modificar Equipo con ID: {equipo_id} ---")
    equipos = leer_equipos()
    equipo_encontrado = False
    for i, equipo in enumerate(equipos):
        if equipo.get('ID') == str(equipo_id):
            print("Equipo actual:")
            for key, value in equipo.items():
                print(f"- {key}: {value}")

            print("\nIngrese los nuevos valores (deje en blanco para mantener el actual):")
            nombre = input(f"Nombre ({equipo['Nombre']}): ")
            tipo = input(f"Tipo ({equipo['Tipo']}): ")
            valor_calibracion = input(f"Valor de Calibración ({equipo['ValorCalibracion']}): ")
            fecha_mantenimiento = input(f"Fecha Último Mantenimiento ({equipo['FechaUltimoMantenimiento']}): ")

            if nombre: equipos[i]['Nombre'] = nombre
            if tipo: equipos[i]['Tipo'] = tipo
            if valor_calibracion: equipos[i]['ValorCalibracion'] = valor_calibracion
            if fecha_mantenimiento: equipos[i]['FechaUltimoMantenimiento'] = fecha_mantenimiento

            guardar_equipos(equipos)
            print("Equipo modificado con éxito.")
            equipo_encontrado = True
            break
    if not equipo_encontrado:
        print(f"No se encontró ningún equipo con el ID '{equipo_id}'.")

# Ejemplo de uso:
# agregar_equipo() # Descomentar para agregar un nuevo equipo
# modificar_equipo(1) # Descomentar para modificar el equipo con ID 1

# MANTENIMIENTO

def equipos_necesitan_mantenimiento(fecha_limite):
    """
    Muestra equipos cuyo último mantenimiento es anterior a una fecha límite.
    fecha_limite debe ser un objeto datetime.date.
    """
    print(f"\n--- Equipos que necesitan mantenimiento antes de: {fecha_limite.strftime('%Y-%m-%d')} ---")
    equipos = leer_equipos()
    encontrados = False
    for equipo in equipos:
        fecha_str = equipo.get('FechaUltimoMantenimiento')
        try:
            fecha_mantenimiento = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            if fecha_mantenimiento < fecha_limite:
                print(f"ID: {equipo['ID']}, Nombre: {equipo['Nombre']}, Último Mant.: {equipo['FechaUltimoMantenimiento']}")
                encontrados = True
        except (ValueError, TypeError):
            print(f"Advertencia: Fecha de mantenimiento inválida para ID {equipo['ID']}: '{fecha_str}'")
    if not encontrados:
        print("No hay equipos que necesiten mantenimiento antes de esta fecha.")

def buscar_equipos_por_tipo(tipo_equipo):
    """
    Busca y lista equipos de un tipo específico.
    """
    print(f"\n--- Buscar Equipos por Tipo: '{tipo_equipo}' ---")
    equipos = leer_equipos()
    encontrados = False
    for equipo in equipos:
        if equipo.get('Tipo', '').lower() == tipo_equipo.lower():
            print(f"ID: {equipo['ID']}, Nombre: {equipo['Nombre']}, Valor Calibración: {equipo['ValorCalibracion']}")
            encontrados = True
    if not encontrados:
        print(f"No se encontraron equipos del tipo '{tipo_equipo}'.")

# Ejemplo de uso:
# fecha_limite_ejemplo = datetime(2023, 11, 1).date() # Equipos con mantenimiento antes del 1 de Noviembre de 2023
# equipos_necesitan_mantenimiento(fecha_limite_ejemplo)

# buscar_equipos_por_tipo('Sensor')