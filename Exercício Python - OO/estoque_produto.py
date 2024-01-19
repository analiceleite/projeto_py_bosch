from item_biblioteca import *
from livro import *
from revista import *
from midia_digital import *

class estoque_produto:
    def __init__(self):
        self.__lista_produto = []
        self.__lista_produto_alugado = []


    def get_lista_produto_alugado(self):
        return self.__lista_produto_alugado
    def set_lista_produto_alugado(self, value):
        self.__lista_produto_alugado = value
    def get_lista_produto(self):
        return self.__lista_produto
    def set_lista_produto(self, value):
        self.__lista_produto = value


    def add_lista_produto(self, produto_em_cadastro):
        self.__lista_produto.append(produto_em_cadastro)
        return True


    def mostrar_lista_produto(self):
        for produto in self.__lista_produto:
            print(produto.get_titulo())

    def atribuir_id(self):
        id = 1
        for produto in self.__lista_produto:
            if (produto.get_id() >= id):
                id = produto.get_id() + 1
        return id

    def exibir_lista_produto(self):
        print("\nLista geral de produtos:")
        for produto in self.__lista_produto:
            print(produto.get_id(),"- "+produto.get_titulo(),sep="") #Implementar (Livro, mídia digital)

    def buscar_produto(self, id):
        print("ENTROU EM BUSCA PRODUTO")
        for produto in self.__lista_produto:
            if(produto.get_id() == id):
                return produto
        return False
