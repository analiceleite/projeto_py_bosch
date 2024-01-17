from item_biblioteca import item_biblioteca
import entrada_saida

class midia_digital(item_biblioteca):
    def __init__(self, id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma, tempo_duracao, categoria) -> None:
        super().__init__(id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma)
        self.__tempo_duracao = tempo_duracao
        self.__categoria = categoria

    def get_tempo_duracao(self):
        return self.__tempo_duracao
    def set_tempo_duracao(self, value):
        self.__tempo_duracao = value
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, value):
        self.__categoria = value
        self.__fabricante = value

    def criar_midia_digital():
        midia_digital_em_cadastro = midia_digital
        
        categoria_temp = entrada_saida.menu_escolher_midia_fisica()
        titulo_temp = entrada_saida.solicitar_cadastro_produto_geral("o titulo")
        genero_temp = entrada_saida.solicitar_cadastro_produto_geral("o gênero")
        autoria_temp = entrada_saida.solicitar_cadastro_produto_geral("a autoria")
        ano_lancamento_temp = entrada_saida.solicitar_cadastro_produto_geral_int("o ano de lançamento")
        tempo_duracao_temp = entrada_saida.solicitar_cadastro_produto_geral_float("a duração em minutos")#Verificar se minuto é maior que 59
        classificacao_indicativa_temp = entrada_saida.solicitar_cadastro_produto_geral_int("a classificação indicativa")
        idioma_temp = entrada_saida.solicitar_cadastro_produto_geral("o idioma")
        tiragem_temp = entrada_saida.solicitar_cadastro_produto_geral_int("a tiragem")
        avaliacao_geral_temp = entrada_saida.solicitar_cadastro_produto_geral_float("a avaliação geral")
    def ler_midia_digital():
        print
    def atualizar_midia_digital():
        print
    def deletar_midia_digital():
        print