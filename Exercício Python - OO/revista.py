from item_biblioteca import item_biblioteca
import entrada_saida
import validacao
import artes_ascii
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
        art = artes_ascii.titulo_revista_em_andamento
        self.set_titulo(entrada_saida.solicitar_cadastro_livro_string(art,"o titulo",False,14))
        self.__volume = entrada_saida.solicitar_cadastro_livro_int(art,"o volume/edição",False)
        self.set_autoria(entrada_saida.solicitar_cadastro_livro_string(art,"a editora",False,14))
        self.set_ano_lancamento(validacao.validar_ano_lancamento(3))
        self.__quant_paginas = entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade de páginas",False)
        self.set_classificacao_indicativa(validacao.validar_classificacao_indicativa())
        self.set_idioma(entrada_saida.solicitar_cadastro_livro_string(art,"o idioma",False,14))
        self.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade disponível",False))
        self.set_locatario(None)
        self.set_tempo_aluguel(None)
        self.set_tipo("Revista")
        self.set_id(estoque.atribuir_id())

        if(validacao.confirmar_cadastro_revista(self,estoque)):
            while (i < self.get_quantidade_disponivel()):
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
    