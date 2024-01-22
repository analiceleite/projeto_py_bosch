from item_biblioteca import *
from livro import *
from revista import *
from midia_digital import *
from gestao_clientes import *

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

    def mostrar_lista_produto(self):
        for produto in self.__lista_produto:
            print(produto.get_titulo())

    def add_lista_produto_alugado(self, produto):
        self.__lista_produto_alugado.append(produto)
        for produto in self.__lista_produto_alugado:
            print(produto.get_titulo())
            #print(produto.get_dono().get_nome())# Método para acessar o nome do dono
        
        

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
        for produto in self.__lista_produto:
            if(produto.get_id() == id):
                validacao.validar_exibicao_busca(produto)
                return produto
        return None
    
    def alugar_produto(self, produto, lista_usuarios,estoque):
        cliente = lista_usuarios.buscar_cliente(entrada_saida.solicitar_rg_aluguel())
        if (cliente):
            tempo_aluguel = validacao.confirmar_tempo_aluguel()
            validacao.confirmar_aluguel(cliente, produto, tempo_aluguel,estoque)
        else:
            print("Cliente não encontrado")


