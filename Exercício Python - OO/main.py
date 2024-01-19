import entrada_saida
from livro import livro
from midia_digital import midia_digital
from revista import revista
from item_biblioteca import item_biblioteca
from estoque_produto import estoque_produto

estoque = estoque_produto()

def main():
    match entrada_saida.menu_principal():
        case 1: #Cadastrar
            match entrada_saida.menu_escolher_tipo_cadastro():
                case 1: #Escolha de categoria do produto
                    match entrada_saida.menu_escolher_tipo_produto():
                        case 1: #Livro
                            livro_em_andamento = livro()
                            livro_em_andamento.criar_livro(estoque)
                            main()
                        case 2: #Mídia digital
                            midia_em_andamento = midia_digital()
                            midia_em_andamento.criar_midia_digital(estoque)
                            main()
                        case 3: #Revista
                            revista_em_andamento = revista()
                            revista_em_andamento.criar_revista(estoque)
                            main()
                        case 4: #Jogos
                            print
                            #Inserir jogos
        case 2: #Buscar
            match entrada_saida.menu_buscar():
                case 1: #Exibir lista geral de produtos
                    estoque.exibir_lista_produto()
                    produto_em_busca = estoque.buscar_produto(entrada_saida.solicitar_id_buscar())
                    match entrada_saida.menu_item_pesquisado():
                        case 1: #Alugar
                            print
                        case 2: #Buscar outro produto
                            print
                        case 3: #Voltar ao menu principal
                            print

                case 2: #Voltar ao menu principal
                    main()

                    






           


main()
