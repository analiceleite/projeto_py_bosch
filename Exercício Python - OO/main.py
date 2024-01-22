import entrada_saida
from livro import livro
from midia_digital import midia_digital
from revista import revista
from item_biblioteca import item_biblioteca
from estoque_produto import estoque_produto
from gestao_clientes import gestao_clientes
from clientes import clientes

estoque = estoque_produto()
lista_usuarios = gestao_clientes()
usuario_em_andamento = clientes()
usuario_em_andamento.set_nome("Admin")
usuario_em_andamento.set_rg("1234")
usuario_em_andamento.set_telefone("4321")
usuario_em_andamento.set_endereco("Teste")
lista_usuarios.adicionar_cliente(usuario_em_andamento)

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
                case 2: #Cliente
                    usuario_em_andamento = clientes()
                    usuario_em_andamento.criar_usuario(lista_usuarios)
                    main()


        case 2: #Buscar
            match entrada_saida.menu_buscar():
                case 1: #Exibir lista geral de produtos
                    while True:
                        estoque.exibir_lista_produto()
                        produto_em_busca = estoque.buscar_produto(entrada_saida.solicitar_id_buscar())
                        match entrada_saida.menu_item_pesquisado():
                            case 1: #Alugar
                                estoque.alugar_produto(produto_em_busca,lista_usuarios,estoque)
                                break
                            case 2: #Buscar outro produto
                                pass
                            case 3: #Voltar ao menu principal
                                main()
                                

                case 2: #Voltar ao menu principal
                    main()

                    
# if __name__ == "__main__":
#     estoque = estoque_produto
#     livro_teste = livro()
#    livro_teste.criar_livro(estoque)
    # entrada_saida.obter_entrada_centralizada_float("teste",False)
main()