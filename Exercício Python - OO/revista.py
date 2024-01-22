from item_biblioteca import item_biblioteca
import entrada_saida
import validacao

class revista(item_biblioteca):
    def __init__(self):
        self.__quant_paginas = None
        self.__volume = None
        self.__lista_revistas = []

    
    def get_lista_revistas(self):
        return self.__lista_revistas
    def set_lista_revistas(self, value):
        self.__lista_revistas = value
    def get_quant_paginas(self):
        return self.__quant_paginas
    def set_quant_paginas(self, value):
        self.__quant_paginas = value
    def get_volume(self):
        return self.__volume
    def set_volume(self, value):
        self.__volume = value

    def criar_revista(self, estoque):
        i = 0
        self.set_titulo(entrada_saida.solicitar_cadastro_livro_string("o titulo"))
        self.__volume = entrada_saida.solicitar_cadastro_livro_int("o volume/edição")
        self.set_autoria(entrada_saida.solicitar_cadastro_livro_string("a editora"))
        self.set_ano_lancamento(validacao.validar_ano_lancamento())
        self.__quant_paginas = entrada_saida.solicitar_cadastro_livro_int("a quantidade de páginas")
        self.set_classificacao_indicativa(validacao.validar_classificacao_indicativa())
        self.set_idioma(entrada_saida.solicitar_cadastro_livro_string("o idioma"))
        self.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int("a quantidade disponível"))
        self.set_locatario(None)
        self.set_tempo_aluguel(None)
        self.set_tipo("Revista")
        self.set_id(estoque.atribuir_id())

        if(validacao.confirmar_cadastro_revista(self,estoque)):
            while (i < self.get_quantidade_disponivel):
                self.add_lista_revista()
                i += 1

    def add_lista_revista(self):
        self.__lista_revistas.append(self)
        print("Adicionou",self.get_locatario())

    def ler_revista():
        print
    def atualizar_revista():
        print
    def deletar_revista():
        print
    