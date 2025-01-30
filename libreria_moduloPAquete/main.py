from libreria.gestion import Libreria
from libreria.productos import Libro

libro1 = Libro("ISBN-1","Asi es la puta vida","Jordi Wild", 20.0 )
libro2 = Libro("ISBN-2","El principito","Autor1", 15.50 )
libro3 = Libro("ISBN-3","EL Libro troll","ElRubius", 22.2 )
libro4 = Libro("ISBN-4","aaa","ElRubius", 17.2 )


libro1.mostrarInfo()

miLibreria = Libreria()

miLibreria.anadirLibro(libro1)

miLibreria.anadirLibro(libro2)

miLibreria.mostrarCatalogo()

miLibreria.anadirLibro(libro3)

miLibreria.mostrarCatalogo()

miLibreria.eliminarLibro("ISBN-2")

miLibreria.mostrarCatalogo()

#filtrar por autor

miLibreria.anadirLibro(libro4)

miLibreria.buscarLibroAutor("ElRubius")

#buscar libro por titulo

miLibreria.buscarLibroTitulo("Asi es la puta vida")






#***************************


"""
# Crear una librería
mi_libreria = Libreria()

# Crear algunos libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "1234567890", 15.50)
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "9876543210", 20.00)

# Añadir libros a la librería
mi_libreria.añadir_libro(libro1)
mi_libreria.añadir_libro(libro2)

# Mostrar todos los libros
print("Catálogo de libros:")
mi_libreria.mostrar_libros()

# Buscar libros por autor
print("Buscar por autor 'Gabriel García Márquez':")
mi_libreria.buscar_por_autor("Gabriel García Márquez")

# Buscar libros por título
print("Buscar por título 'El Quijote':")
mi_libreria.buscar_por_titulo("El Quijote")

# Eliminar un libro
mi_libreria.eliminar_libro("1234567890")

# Mostrar libros después de la eliminación
print("Catálogo de libros después de eliminar uno:")
mi_libreria.mostrar_libros()
"""