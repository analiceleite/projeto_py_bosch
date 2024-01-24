import os
class gestao_clientes:
    def __init__(self):
        self.__lista_cliente = []

    def get_lista_usuarios(self):
        return self.__lista_cliente
    def set_lista_usuarios(self, value):
        self.__lista_cliente = value
    
    def adicionar_cliente(self, cliente_em_cadastro):
        self.__lista_cliente.append(cliente_em_cadastro)

    def buscar_cliente(self, rg):
        for cliente in self.get_lista_usuarios():
            if(cliente.get_rg() == str(rg)):
                return cliente
        return False