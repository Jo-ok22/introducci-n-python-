import sys
sys.stdout.reconfigure(encoding='utf-8')



# Diccionarios para almacenar información
estudiantes = {}  # Contendrá datos personales de los estudiantes
materias = {}     # Contendrá las materias inscritas por cada estudiante
calificaciones = {}  # Contendrá las calificaciones por materia de cada estudiante

# Funciones del sistema
def registrar_estudiante(nombre, edad, carrera):
    """
    Registra un estudiante con sus datos básicos.
    """
    estudiantes[nombre] = {'edad': edad, 'carrera': carrera}
    materias[nombre] = []  # Inicializa una lista vacía de materias para el estudiante
    calificaciones[nombre] = {}  # Inicializa un diccionario vacío para calificaciones
    print(f"Estudiante {nombre} registrado.")

def registrar_materia(estudiante, materia):
    """
    Añade una materia a un estudiante.
    """
    if estudiante in materias:
        materias[estudiante].append(materia)  # Agrega la materia a la lista del estudiante
        calificaciones[estudiante][materia] = []  # Inicializa una lista vacía para calificaciones de la materia
        print(f"Materia {materia} añadida para {estudiante}.")
    else:
        print(f"Estudiante {estudiante} no encontrado.")

def agregar_calificacion(estudiante, materia, calificacion):
    """
    Añade una calificación a una materia específica de un estudiante.
    """
    if estudiante in calificaciones and materia in calificaciones[estudiante]:
        calificaciones[estudiante][materia].append(calificacion)  # Añade la calificación a la lista
        print(f"Calificación {calificacion} añadida para {materia} de {estudiante}.")
    else:
        print(f"Materia {materia} o estudiante {estudiante} no encontrado.")

def calcular_promedio(estudiante):
    """
    Calcula el promedio de calificaciones de un estudiante.
    """
    if estudiante in calificaciones:
        total, count = 0, 0
        for notas in calificaciones[estudiante].values():
            total += sum(notas)  # Suma todas las calificaciones
            count += len(notas)  # Cuenta el número total de calificaciones
        return total / count if count > 0 else 0  # Evita dividir por 0
    else:
        return 0

def mostrar_estadisticas():
    """
    Muestra las estadísticas de todos los estudiantes registrados.
    """
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante)  # Calcula el promedio del estudiante
        print(f"Estudiante: {estudiante}")
        print(f"  Materias: {materias[estudiante]}")
        print(f"  Promedio: {promedio:.2f}")
    print("-" * 30)

# Programa principal: ejemplo de uso
registrar_estudiante("Juan", 20, "Ingeniería")
registrar_estudiante("María", 22, "Medicina")

registrar_materia("Juan", "Matemáticas")
registrar_materia("Juan", "Física")
registrar_materia("María", "Biología")

agregar_calificacion("Juan", "Matemáticas", 90)
agregar_calificacion("Juan", "Física", 80)
agregar_calificacion("María", "Biología", 85)

mostrar_estadisticas()