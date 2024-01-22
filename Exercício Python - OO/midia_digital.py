from item_biblioteca import item_biblioteca
import entrada_saida
import validacao

class midia_digital(item_biblioteca):
    def __init__(self):
        self.__tempo_duracao = None
        self.__categoria = None
        self.__lista_midia_digital = []

    def get_lista_midia_digital(self):
        return self.__lista_midia_digital
    def set_lista_midia_digital(self, value):
        self.__lista_midia_digital = value
    def get_tempo_duracao(self):
        return self.__tempo_duracao
    def set_tempo_duracao(self, value):
        self.__tempo_duracao = value
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, value):
        self.__categoria = value

    def criar_midia_digital(self,estoque):
        i = 0

        self.__categoria = entrada_saida.solicitar_categoria_midia()
        self.set_titulo(entrada_saida.solicitar_cadastro_livro_string("o titulo"))
        self.set_autoria(entrada_saida.solicitar_cadastro_livro_string("a autoria"))
        self.set_ano_lancamento(validacao.validar_ano_lancamento())
        self.__tempo_duracao = entrada_saida.solicitar_cadastro_livro_int("a duração em minutos")#Validações
        self.set_classificacao_indicativa(validacao.validar_classificacao_indicativa())
        self.set_idioma(entrada_saida.solicitar_cadastro_livro_string("o idioma"))
        self.set_tiragem(entrada_saida.solicitar_cadastro_livro_int("a tiragem"))
        self.set_avaliacao_geral(validacao.validar_avaliacao_produtos(self))
        self.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int("a quantidade disponível"))
        self.set_tipo("Mídia Digital")
        self.set_locatario(None)
        self.set_tempo_aluguel(None)
        self.set_id(estoque.atribuir_id())

        if(validacao.confirmar_cadastro_midia(self, estoque)):
            while (i < self.get_quantidade_disponivel()):
                self.add_lista_midia_digital()
                i += 1

    def add_lista_midia_digital(self):
        self.__lista_midia_digital.append(self)
        print("Adicionou",self.get_locatario())
    def ler_midia_digital():
        print
    def atualizar_midia_digital():
        print
    def deletar_midia_digital():
        print