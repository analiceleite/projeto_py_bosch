class estoque_produto:
    def __init__(self):
        self.__lista_produto = []

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
            
        
        
        