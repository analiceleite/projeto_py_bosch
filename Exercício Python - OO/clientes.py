import entrada_saida
import validacao

class clientes:
    def __init__(self):
        self.__nome = None
        self.__rg = None
        self.__endereco = None
        self.__telefone = None

    def get_nome(self):
        return self.__nome
    def set_nome(self, value):
        self.__nome = value
    def get_rg(self):
        return self.__rg
    def set_rg(self, value):
        self.__rg = value
    def get_endereco(self):
        return self.__endereco
    def set_endereco(self, value):
        self.__endereco = value
    def get_telefone(self):
        return self.__telefone
    def set_telefone(self, value):
        self.__telefone = value

    def criar_usuario(self, lista_usuarios):
        self.set_nome(entrada_saida.solicitar_dados_cliente("nome"))
        self.set_rg(entrada_saida.solicitar_dados_cliente("RG"))
        self.set_telefone(entrada_saida.solicitar_dados_cliente("telefone"))
        self.set_endereco(entrada_saida.solicitar_dados_cliente("endereço"))

        validacao.confirmar_cadastro_cliente(self, lista_usuarios)