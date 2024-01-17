import entrada_saida
from livro import livro

def Main():
    match entrada_saida.menu_principal():
        case 1: #Escolha do tipo de cadastro
            match entrada_saida.menu_escolher_tipo_cadastro():
                case 1: #Escolha de categoria do produto
                    match entrada_saida.menu_escolher_categoria("principal"):
                        case 1: #Livro
                            livro.criar_livro()
