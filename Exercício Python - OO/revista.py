from item_biblioteca import item_biblioteca
import entrada_saida
import validacao

class revista(item_biblioteca):
    def __init__(self):
        self.__quant_paginas = None
        self.__volume = None

    def get_quant_paginas(self):
        return self.__quant_paginas
    def set_quant_paginas(self, value):
        self.__quant_paginas = value
    def get_volume(self):
        return self.__volume
    def set_volume(self, value):
        self.__volume = value

    def criar_revista(self, estoque):
        
        self.set_titulo(entrada_saida.solicitar_cadastro_produto_geral("o titulo"))
        self.__volume = entrada_saida.solicitar_cadastro_produto_geral_int("o volume/edição")
        self.set_autoria(entrada_saida.solicitar_cadastro_produto_geral("a editora"))
        self.set_ano_lancamento(entrada_saida.solicitar_cadastro_produto_geral_int("o ano de lançamento"))
        self.__quant_paginas = entrada_saida.solicitar_cadastro_produto_geral_int("a quantidade de páginas")
        self.set_classificacao_indicativa(entrada_saida.solicitar_cadastro_produto_geral_int("a classificação indicativa"))
        self.set_idioma(entrada_saida.solicitar_cadastro_produto_geral("o idioma"))
        self.set_tipo("Revista")

        validacao.confirmar_cadastro_revista(self,estoque)

    def ler_revista():
        print
    def atualizar_revista():
        print
    def deletar_revista():
        print
    