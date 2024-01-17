import Livro
class ItemBiblioteca:
    def __init__(self, titulo, autor, ano_publicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao

    def get_titulo(self):
        return self.__titulo


    def set_titulo(self, value):
        self.__titulo = value


    def get_autor(self):
        return self.__autor

    def set_autor(self, value):
        self.__autor = value

    
    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def set_ano_publicacao(self, value):
        self.__ano_publicacao = value

        
        