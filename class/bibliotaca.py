
class libro:

    contador_libros = 0

    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas

        libro.contador_libros += 1
    def mostrar_info(self):
        return self.titulo,self.autor,self.paginas

    @staticmethod
    def es_grade(libro):
        if libro.paginas>300:
            return True
        else:
            return False
        
    @classmethod
    def total_libros(cls): 
        return cls.contador_libros
    

    pass
