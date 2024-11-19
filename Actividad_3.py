import sys
sys.stdout.reconfigure(encoding='utf-8')


# Diccionarios para almacenar información
usuarios = {}  # Datos personales de los usuarios
libros = {}    # Información de los libros
prestamos = {}  # Préstamos realizados por los usuarios

# Funciones del sistema
def registrar_usuario(usuarios, nombre, edad, email):
    """
    Registra un usuario con sus datos básicos.
    """
    usuarios[nombre] = {'edad': edad, 'email': email}
    prestamos[nombre] = []  # Inicializa una lista vacía de préstamos para el usuario
    print(f"Usuario {nombre} registrado.")

def registrar_libro(libros, titulo, autor, genero):
    """
    Registra un libro con su información básica.
    """
    libros[titulo] = {'autor': autor, 'genero': genero}
    print(f"Libro '{titulo}' registrado.")

def realizar_prestamo(prestamos, usuarios, libros, usuario, titulo_libro, fecha):
    """
    Registra un préstamo de libro realizado por un usuario.
    """
    if usuario in usuarios and titulo_libro in libros:
        prestamos[usuario].append((titulo_libro, fecha))  # Añade una tupla con el libro y la fecha
        print(f"Préstamo registrado: {usuario} tomó '{titulo_libro}' el {fecha}.")
    else:
        print(f"Usuario o libro no encontrado.")

def calcular_prestamos_usuario(prestamos, usuario):
    """
    Calcula la cantidad total de préstamos realizados por un usuario.
    """
    return len(prestamos.get(usuario, []))

def mostrar_estadisticas(prestamos):
    """
    Muestra estadísticas de préstamos realizados.
    """
    print("--- Estadísticas ---")
    for usuario, lista_prestamos in prestamos.items():
        print(f"{usuario}: {len(lista_prestamos)} préstamo(s).")

    # Determinar el libro más solicitado
    libros_solicitados = {}
    for lista in prestamos.values():
        for titulo, _ in lista:
            libros_solicitados[titulo] = libros_solicitados.get(titulo, 0) + 1

    if libros_solicitados:
        libro_mas_solicitado = max(libros_solicitados, key=libros_solicitados.get)
        print(f"El libro más solicitado es '{libro_mas_solicitado}'.")
    else:
        print("No se han realizado préstamos aún.")
    print("-" * 30)

# Programa principal: ejemplo de uso
registrar_usuario(usuarios, "Juan Pérez", 25, "juanperez@mail.com")
registrar_usuario(usuarios, "María López", 30, "marialopez@mail.com")
registrar_usuario(usuarios, "Carlos García", 28, "carlosgarcia@mail.com")

registrar_libro(libros, "El Quijote", "Miguel de Cervantes", "Novela")
registrar_libro(libros, "1984", "George Orwell", "Distopía")
registrar_libro(libros, "La Odisea", "Homero", "Épica")

realizar_prestamo(prestamos, usuarios, libros, "Juan Pérez", "El Quijote", "2024-11-01")
realizar_prestamo(prestamos, usuarios, libros, "María López", "1984", "2024-11-02")
realizar_prestamo(prestamos, usuarios, libros, "Carlos García", "La Odisea", "2024-11-03")
realizar_prestamo(prestamos, usuarios, libros, "Juan Pérez", "1984", "2024-11-04")
realizar_prestamo(prestamos, usuarios, libros, "María López", "El Quijote", "2024-11-05")

mostrar_estadisticas(prestamos)