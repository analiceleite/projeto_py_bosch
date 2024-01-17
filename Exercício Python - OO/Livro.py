from item_biblioteca import item_biblioteca
import entrada_saida

class livro(item_biblioteca):
    def __init__(self, id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma, quant_paginas, genero, is_best_seller) -> None:
        super().__init__(id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma)
        self.__quant_paginas = quant_paginas
        self.__genero = genero
        self.__is_best_seller = is_best_seller

#Getter & Setters
    def get_quant_paginas(self):
        return self.__quant_paginas
    def set_quant_paginas(self, value):
        self.__quant_paginas = value
    def get_genero(self):
        return self.__genero
    def set_genero(self, value):
        self.__genero = value
    def get_is_best_seller(self):
        return self.__is_best_seller
    def set_is_best_seller(self, value):
        self.__is_best_seller = value

    def criar_livro(self):

        self.set_titulo(entrada_saida.solicitar_cadastro_produto_geral("o titulo"))
        self.set_genero(entrada_saida.solicitar_cadastro_produto_geral("o gênero"))
        self.set_autoria(entrada_saida.solicitar_cadastro_produto_geral("a autoria"))
        self.set_ano_lancamento(entrada_saida.solicitar_cadastro_produto_geral_int("o ano de lançamento")) #Validar número negativo
        self.set_quant_paginas(entrada_saida.solicitar_cadastro_produto_geral_int("a quantidade de páginas"))#Validar número negativo
        self.set_classificacao_indicativa(entrada_saida.solicitar_cadastro_produto_geral_int("a classificação indicativa")) #Validar número negativo
        self.set_idioma(entrada_saida.solicitar_cadastro_produto_geral("o idioma"))
        self.set_tiragem(entrada_saida.solicitar_cadastro_produto_geral_int("a tiragem")) #Validar número negativo
        self.set_avaliacao_geral(entrada_saida.solicitar_cadastro_produto_geral_float("a avaliação geral")) #Validar número negativo
        self.set_is_best_seller(entrada_saida.solicitar_best_seller())
        

#del objeto
    def ler_livro():
        print
    def atualizar_livro():
        print
    def deletar_livro():
        print
