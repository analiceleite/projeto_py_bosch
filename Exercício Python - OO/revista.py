from item_biblioteca import item_biblioteca
import entrada_saida

class revista(item_biblioteca):
    def __init__(self, id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma,quant_paginas, volume) -> None:
        super().__init__(id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma)
        self.__quant_paginas = quant_paginas
        self.__volume = volume

    def get_quant_paginas(self):
        return self.__quant_paginas
    def set_quant_paginas(self, value):
        self.__quant_paginas = value
    def get_volume(self):
        return self.__volume
    def set_volume(self, value):
        self.__volume = value

        self.__cartas_leitores = value

    def criar_revista():
        revista_em_cadastro = revista

        titulo_temp = entrada_saida.solicitar_cadastro_produto_geral("o titulo")
        volume_temp = entrada_saida.solicitar_cadastro_produto_geral_int("o volume/edição")
        genero_temp = entrada_saida.solicitar_cadastro_produto_geral("o gênero")
        autoria_temp = entrada_saida.solicitar_cadastro_produto_geral("a editora")
        ano_lancamento_temp = entrada_saida.solicitar_cadastro_produto_geral_int("o ano de lançamento")
        quant_paginas_temp = entrada_saida.solicitar_cadastro_produto_geral_int("a quantidade de páginas")
        classificacao_indicativa_temp = entrada_saida.solicitar_cadastro_produto_geral_int("a classificação indicativa")
        idioma_temp = entrada_saida.solicitar_cadastro_produto_geral("o idioma")
        tiragem_temp = entrada_saida.solicitar_cadastro_produto_geral_int("a tiragem")

    def ler_revista():
        print
    def atualizar_revista():
        print
    def deletar_revista():
        print
    