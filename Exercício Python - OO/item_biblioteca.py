class item_biblioteca:
    def __init__(self, id, titulo, autoria, ano_lancamento, classificacao_indicativa, tiragem, avaliacao_geral, idioma) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__autoria = autoria
        self.__ano_lancamento = ano_lancamento
        self.__classificacao_indicativa = classificacao_indicativa
        self.__tiragem = tiragem
        self.__avaliacao_geral = avaliacao_geral
        self.__idioma = idioma

#Getter & Setters
    def get_id(self):
        return self.__id
    def set_id(self, value):
        self.__id = value
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
    def get_classificacao_indicativa(self):
        return self.__classificacao_indicativa
    def set_classificacao_indicativa(self, value):
        self.__classificacao_indicativa = value
    def get_tiragem(self):
        return self.__tiragem
    def set_tiragem(self, value):
        self.__tiragem = value
    def get_avaliacao_geral(self):
        return self.__avaliacao_geral
    def set_avaliacao_geral(self, value):
        self.__avaliacao_geral = value
    def get_idioma(self):
        return self.__idioma
    def set_idioma(self, value):
        self.__idioma = value


