import ItemBiblioteca
class Livro(ItemBiblioteca.ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, quant_paginas):
        super().__init__(titulo, autor, ano_publicacao)
        self.__quant_paginas = quant_paginas
    
    def get_quant_paginas(self):
        return self.__quant_paginas

    
    def set_quant_paginas(self, value):
        self.__quant_paginas = value

    # def get_titulo(self):
    #     return self.__titulo

    # def set_titulo(self, value):
    #     self.__titulo = value


    # def get_autor(self):
    #     return self.__autor

    # def set_autor(self, value):
    #     self.__autor = value

    
    # def get_ano_publicacao(self):
    #     return self.__ano_publicacao

    
    # def set_ano_publicacao(self, value):
    #     self.__ano_publicacao = value