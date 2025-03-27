import random

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.lecturas_usuario = {}  # Registro de libros leídos por cada usuario
        self.reseñas = {}  # Almacena reseñas y puntuaciones de los libros

    # Agregar un libro a la biblioteca
    def agregar_libro(self, titulo, autor, cantidad):
        if titulo not in self.libros:
            self.libros[titulo] = {"autor": autor, "cantidad": cantidad}
        else:
            self.libros[titulo]["cantidad"] += cantidad
        print(f"Libro '{titulo}' agregado con {cantidad} copias disponibles.")
    
    # Prestar un libro (reduce su cantidad)
    def prestar_libro(self, titulo):
        if titulo in self.libros and self.libros[titulo]["cantidad"] > 0:
            self.libros[titulo]["cantidad"] -= 1
            print(f"Libro '{titulo}' prestado. Quedan {self.libros[titulo]['cantidad']} copias disponibles.")
        else:
            print(f"El libro '{titulo}' no está disponible.")
    
    # Devolver un libro (aumenta su cantidad)
    def devolver_libro(self, titulo):
        if titulo in self.libros:
            self.libros[titulo]["cantidad"] += 1
            print(f"Libro '{titulo}' devuelto. Ahora hay {self.libros[titulo]['cantidad']} copias disponibles.")
        else:
            print(f"El libro '{titulo}' no está en la biblioteca.")
    
    # Consultar si un libro está disponible
    def consultar_disponibilidad(self, titulo):
        if titulo in self.libros:
            if self.libros[titulo]["cantidad"] > 0:
                print(f"El libro '{titulo}' está disponible.")
            else:
                print(f"El libro '{titulo}' no está disponible.")
        else:
            print(f"El libro '{titulo}' no existe en la biblioteca.")
    
    # Sugerir un libro en base a las lecturas anteriores
    def sugerir_libro(self, usuario):
        if usuario not in self.lecturas_usuario or not self.lecturas_usuario[usuario]:
            print(f"Lo siento, no tenemos suficiente información sobre las lecturas de {usuario}.")
            return

        # Obtenemos los títulos de los libros leídos por el usuario
        libros_leidos = self.lecturas_usuario[usuario]
        sugerencias = []

        # Sugerir libros basados en autor similar
        for titulo in libros_leidos:
            autor = self.libros[titulo]["autor"]
            for libro, info in self.libros.items():
                if info["autor"] == autor and libro not in libros_leidos:
                    sugerencias.append(libro)
        
        if sugerencias:
            sugerido = random.choice(sugerencias)
            print(f"Te sugerimos leer: '{sugerido}'")
        else:
            print(f"No tenemos libros similares a los que has leído anteriormente.")
    
    # Registrar una reseña para un libro
    def registrar_resena(self, titulo, puntuacion, comentario=""):
        if titulo not in self.libros:
            print(f"El libro '{titulo}' no existe en la biblioteca.")
            return
        
        if titulo not in self.reseñas:
            self.reseñas[titulo] = {"puntuaciones": [], "comentarios": []}
        
        self.reseñas[titulo]["puntuaciones"].append(puntuacion)
        self.reseñas[titulo]["comentarios"].append(comentario)
        
        print(f"Reseña registrada para '{titulo}' con puntuación {puntuacion}.")
    
    # Ver el promedio de puntuación de un libro
    def ver_promedio_resena(self, titulo):
        if titulo in self.reseñas:
            puntuaciones = self.reseñas[titulo]["puntuaciones"]
            promedio = sum(puntuaciones) / len(puntuaciones) if puntuaciones else 0
            print(f"El promedio de puntuación de '{titulo}' es: {promedio}")
        else:
            print(f"No hay reseñas disponibles para '{titulo}'.")

# Funcionalidad adicional: Ranking de libros más prestados
    def ranking_libros(self):
        ranking = sorted(self.libros.items(), key=lambda x: x[1]["cantidad"], reverse=True)
        print("Ranking de los libros más prestados:")
        for titulo, info in ranking:
            print(f"{titulo}: {info['cantidad']} copias disponibles")

# Función para permitir al usuario agregar nuevos libros (sin necesidad de respuesta de sí/no)
def agregar_libro_usuario(biblioteca):
    print("\nVamos a agregar un nuevo libro a la biblioteca.")
    print("Introduce el título del libro:")
    titulo = input()
    print("Introduce el autor del libro:")
    autor = input()
    print("Introduce la cantidad de copias disponibles:")
    cantidad = int(input())
    biblioteca.agregar_libro(titulo, autor, cantidad)
    
    # Después de agregar, automáticamente se presta el libro
    print(f"\n¡El libro '{titulo}' ha sido agregado! Ahora lo vamos a prestar...")
    biblioteca.prestar_libro(titulo)
    
    # Repetir el proceso con el nuevo libro
    biblioteca.devolver_libro(titulo)
    biblioteca.consultar_disponibilidad(titulo)
    
    # Registrar reseñas
    biblioteca.registrar_resena(titulo, 4, "Interesante libro, recomendable.")
    biblioteca.ver_promedio_resena(titulo)

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("El Quijote", "Miguel de Cervantes", 5)
biblioteca.agregar_libro("1984", "George Orwell", 3)
biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 4)

# Simulamos algunas operaciones iniciales
biblioteca.prestar_libro("El Quijote")
biblioteca.devolver_libro("El Quijote")
biblioteca.consultar_disponibilidad("1984")

# Simulación de lecturas y sugerencias
biblioteca.lecturas_usuario["Juan"] = ["El Quijote", "1984"]
biblioteca.sugerir_libro("Juan")

# Permitir al usuario agregar un libro sin depender de "sí/no"
agregar_libro_usuario(biblioteca)

# Ver ranking de libros más prestados
biblioteca.ranking_libros()