import entrada_saida
from livro import livro
from midia_digital import midia_digital
from revista import revista

def Main():
    match entrada_saida.menu_principal():
        case 1: #Escolha do tipo de cadastro
            match entrada_saida.menu_escolher_tipo_cadastro():
                case 1: #Escolha de categoria do produto
                    match entrada_saida.menu_escolher_tipo_produto():
                        case 1: #Livro
                            livro_em_andamento = livro()
                            livro_em_andamento.criar_livro()
                            
                        case 2:
                            midia_digital.criar_midia_digital()
                        case 3:
                            revista.criar_revista()
                        case 4:
                            print
                            #inserir jogos


Main()
