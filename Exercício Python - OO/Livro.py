from item_biblioteca import item_biblioteca
import entrada_saida
import validacao
import artes_ascii

class livro(item_biblioteca):
    def __init__(self):
        self.__quant_paginas = None
        self.__genero = None
        self.__is_best_seller = None
        self.__lista_livros = []

#Getter & Setters        
    def get_lista_livros(self):
        return self.__lista_livros
    def set_lista_livros(self, value):
        self.__lista_livros = value
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

    def criar_livro(self,estoque):
        i = 0
        art = artes_ascii.titulo_livro_em_andamento
        self.set_titulo(entrada_saida.solicitar_cadastro_livro_string(art, "o titulo", False, 14)) #-- Finalizado    
        self.__genero = entrada_saida.solicitar_categoria_livro() #-- Finalizado
        self.set_autoria(entrada_saida.solicitar_cadastro_livro_string(art,"a autoria", False, 14)) #-- Finalizado
        self.set_ano_lancamento(validacao.validar_ano_lancamento(1)) #-- Finalizado
        self.__quant_paginas = entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade de páginas", False) #--Finalizado
        self.set_classificacao_indicativa(validacao.validar_classificacao_indicativa()) #-- Finalizado
        self.set_idioma(entrada_saida.solicitar_cadastro_livro_string(art,"o idioma", False, 14)) #-- Finalizado
        self.set_tiragem(entrada_saida.solicitar_cadastro_livro_int(art,"a tiragem", False)) #-- Finalizado
        self.set_avaliacao_geral(validacao.validar_avaliacao_produtos(1,self)) #-- Finalizado
        self.__is_best_seller = validacao.valida_best_seller() #-- Em andamento
        self.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade disponível", False))
        self.set_locatario(None)
        self.set_tempo_aluguel(None)
        self.set_tipo("Livro")
        self.set_id(estoque.atribuir_id())
        
        if(validacao.confirmar_cadastro_livro(self,estoque)):
            while (i < self.get_quantidade_disponivel()):
                self.add_lista_livro()
                i+=1
                


    def add_lista_livro(self):
        self.__lista_livros.append(self)
        #print("Adicionou",self.get_locatario())
    def ler_livro():
        print
    def atualizar_livro():
        print
    def deletar_livro():
        print
