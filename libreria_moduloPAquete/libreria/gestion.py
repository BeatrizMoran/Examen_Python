from .productos import Libro

class Libreria:

    def __init__(self):
        self.catalogo = []
    
    def anadirLibro(self, libro: Libro):
        self.catalogo.append(libro)

    def eliminarLibro(self, isbn: str):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                break
    
    def mostrarCatalogo(self):
        catalogo = "\nCatalogo de libros:"
        contador = 1
        if len(self.catalogo) > 0:
            for libro in self.catalogo:
                catalogo +="\nLibro: " + str(contador) + "\nTitulo: " + libro.titulo + "\nAutor:" + libro.autor + "\nPrecio:" + str(libro.precio) + "\n ************* \n"
                contador+=1
            print(catalogo)
        else:
            print("No hay libros en el catalogo")
    
    def buscarLibroAutor(self, autor: str):
        catalogo = "Libros del autor: " + autor
        contador = 1

        for libro in self.catalogo:
            if libro.autor == autor:
                catalogo +="\nLibro: " + str(contador) + "\nTitulo: " + libro.titulo + "\nAutor:" + libro.autor + "\nPrecio:" + str(libro.precio) + "\n ************* \n"
                contador += 1
        
        print(catalogo)
    def buscarLibroTitulo(self, titulo: str)-> str:
        datosLibro = ""
        for libro in self.catalogo:
            if libro.titulo == titulo:
                datosLibro +="\nLibro: " + "\nTitulo: " + libro.titulo + "\nAutor:" + libro.autor + "\nPrecio:" + str(libro.precio) + "\n ************* \n"
                break
        print(datosLibro)

"""
# gestion.py
from productos import Libro  # Importamos la clase Libro del módulo productos

class Libreria:
    def __init__(self):
        self.catalogo = []
    
    def añadir_libro(self, libro: Libro):
        self.catalogo.append(libro)
    
    def eliminar_libro(self, isbn: str):
        self.catalogo = [libro for libro in self.catalogo if libro.isbn != isbn]
    
    def mostrar_libros(self):
        if not self.catalogo:
            print("No hay libros en el catálogo.")
        for libro in self.catalogo:
            libro.mostrar_info()
            print()
    
    def buscar_por_autor(self, autor: str):
        libros_autor = [libro for libro in self.catalogo if libro.autor.lower() == autor.lower()]
        if libros_autor:
            for libro in libros_autor:
                libro.mostrar_info()
                print()
        else:
            print("No se encontraron libros de este autor.")
    
    def buscar_por_titulo(self, titulo: str):
        libros_titulo = [libro for libro in self.catalogo if libro.titulo.lower() == titulo.lower()]
        if libros_titulo:
            for libro in libros_titulo:
                libro.mostrar_info()
                print()
        else:
            print("No se encontraron libros con este título.")

"""