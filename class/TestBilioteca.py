from bibliotaca import libro

libro1 = libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro3 = libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

print(f"Libro1: {libro1.mostrar_info()}")
print(f"Libro1: {libro2.mostrar_info()}")
print(f"Libro1: {libro3.mostrar_info()}")

print(f"¿'{libro1.titulo}' es grande?:", libro.es_grade(libro1))
print(f"¿'{libro2.titulo}' es grande?:", libro.es_grade(libro2))
print(f"¿'{libro3.titulo}' es grande?:", libro.es_grade(libro3))


print("Total de libros creados:", libro.total_libros())
