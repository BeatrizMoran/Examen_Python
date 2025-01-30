class Libro:
    isbn: str
    titulo: str
    autor: str
    precio: float

    def __init__(self, isbn, titulo, autor, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrarInfo(self):
        print("Informacion sobre el libro:", "\nTitulo: ", self.titulo, "\nAutor:", self.autor, "\nPrecio:", self.precio)
    
