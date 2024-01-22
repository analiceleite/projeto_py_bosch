class gestao_clientes:
    def __init__(self):
        self.__lista_cliente = []

    def get_lista_usuarios(self):
        return self.__lista_cliente
    def set_lista_usuarios(self, value):
        self.__lista_cliente = value
    
    def adicionar_cliente(self, cliente_em_cadastro):
        print("ADICIONOU")
        self.__lista_cliente.append(cliente_em_cadastro)
        for cliente in self.__lista_cliente:
            print(cliente.get_nome())
            print(cliente.get_rg())
            print(cliente.get_telefone())
            print(cliente.get_endereco())
    
    def buscar_cliente(self, rg):
        for cliente in self.__lista_cliente:
            if(cliente.get_rg() == rg):
                print("ACHOU CLIENTE")
                return cliente
            else:
                return False