class item_biblioteca:
    def __init__(self, id, preco, titulo, autoria, ano_lancamento, faixa_etaria, dimensoes, tiragem, premios, avaliacao_geral, idioma) -> None:
        self.__id = id
        self.__preco = preco
        self.__titulo = titulo
        self.__autoria = autoria
        self.__ano_lancamento = ano_lancamento
        self.__faixa_etaria = faixa_etaria
        self.__dimensoes = dimensoes
        self.__tiragem = tiragem
        self.__premios = premios
        self.__avaliacao_geral = avaliacao_geral
        self.__idioma = idioma

#Getter & Setters
    def get_id(self):
        return self.__id
    def set_id(self, value):
        self.__id = value
    def get_preco(self):
        return self.__preco
    def set_preco(self, value):
        self.__preco = value
    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, value):
        self.__titulo = value
    def get_autoria(self):
        return self.__autoria
    def set_autoria(self, value):
        self.__autoria = value
    def get_ano_lancamento(self):
        return self.__ano_lancamento
    def set_ano_lancamento(self, value):
        self.__ano_lancamento = value
    def get_faixa_etaria(self):
        return self.__faixa_etaria
    def set_faixa_etaria(self, value):
        self.__faixa_etaria = value
    def get_dimensoes(self):
        return self.__dimensoes
    def set_dimensoes(self, value):
        self.__dimensoes = value
    def get_tiragem(self):
        return self.__tiragem
    def set_tiragem(self, value):
        self.__tiragem = value
    def get_premios(self):
        return self.__premios
    def set_premios(self, value):
        self.__premios = value
    def get_avaliacao_geral(self):
        return self.__avaliacao_geral
    def set_avaliacao_geral(self, value):
        self.__avaliacao_geral = value
    def get_idioma(self):
        return self.__idioma
    def set_idioma(self, value):
        self.__idioma = value


