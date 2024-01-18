from item_biblioteca import item_biblioteca
import entrada_saida
import validacao

class midia_digital(item_biblioteca):
    def __init__(self):
        self.__tempo_duracao = None
        self.__categoria = None

    def get_tempo_duracao(self):
        return self.__tempo_duracao
    def set_tempo_duracao(self, value):
        self.__tempo_duracao = value
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, value):
        self.__categoria = value

    def criar_midia_digital(self,estoque):
        
        self.__categoria = entrada_saida.menu_solicitar_categoria_midia()
        self.set_titulo(entrada_saida.solicitar_cadastro_produto_geral("o titulo"))
        self.set_autoria(entrada_saida.solicitar_cadastro_produto_geral("a autoria"))
        self.set_ano_lancamento(entrada_saida.solicitar_cadastro_produto_geral_int("o ano de lançamento"))
        self.__tempo_duracao = entrada_saida.solicitar_cadastro_produto_geral("a duração")#Verificar se minuto é maior que 59
        self.set_classificacao_indicativa(entrada_saida.solicitar_cadastro_produto_geral_int("a classificação indicativa"))
        self.set_idioma(entrada_saida.solicitar_cadastro_produto_geral("o idioma"))
        self.set_tiragem(entrada_saida.solicitar_cadastro_produto_geral_int("a tiragem"))
        self.set_avaliacao_geral(entrada_saida.solicitar_cadastro_produto_geral_float("a avaliação geral"))

        validacao.confirmar_cadastro_midia(self, estoque)

    def ler_midia_digital():
        print
    def atualizar_midia_digital():
        print
    def deletar_midia_digital():
        print