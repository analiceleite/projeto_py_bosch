from item_biblioteca import item_biblioteca

class livro(item_biblioteca):
    def __init__(self, id, preco, titulo, autoria, ano_lancamento, faixa_etaria, dimensoes, tiragem, premios, avaliacao_geral, idioma, quant_paginas, genero, is_best_seller) -> None:
        super().__init__(id, preco, titulo, autoria, ano_lancamento, faixa_etaria, dimensoes, tiragem, premios, avaliacao_geral, idioma)
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

    def criar_livro():
        livro_em_andamento = livro
        print()


    def ler_livro():
        print
    def atualizar_livro():
        print
    def deletar_livro():
        print