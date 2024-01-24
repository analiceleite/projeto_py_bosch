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
livrinho = livro()
usuario_em_andamento = clientes()
usuario_em_andamento.set_nome("João")
usuario_em_andamento.set_rg("1234567")
usuario_em_andamento.set_telefone("4321")
usuario_em_andamento.set_endereco("Teste") 
lista_usuarios.adicionar_cliente(usuario_em_andamento)

def main():
    while True:
        match entrada_saida.menu_principal(17, False):
            case 1: #Cadastrar
                match entrada_saida.menu_escolher_tipo_cadastro(16, False):
                    case 1: #Escolha de categoria do produto
                        match entrada_saida.menu_escolher_tipo_produto(18, False):
                            case 1: #Livro 100%
                                livro_em_andamento = livro()
                                livro_em_andamento.criar_livro(estoque)
                                main()
                            case 2: #Mídia digital 100%
                                midia_em_andamento = midia_digital()
                                midia_em_andamento.criar_midia_digital(estoque)
                                main()
                            case 3: #Revista 100%
                                revista_em_andamento = revista()
                                revista_em_andamento.criar_revista(estoque)
                                main()
                            case 4: #Jogos...
                                print
                                #Inserir jogos
                            case 5:
                                main()
                    case 2: #Cliente
                        usuario_em_andamento = clientes()
                        usuario_em_andamento.criar_usuario(lista_usuarios)
                        main()


            case 2: #Buscar
                match estoque_produto.opcao_menu_busca(len(estoque.get_lista_produto())):
                    case 1: #Exibir lista geral de produtos
                        estoque_produto.exibir_lista_geral(estoque,lista_usuarios)
                    case _:
                        main()
            case 3:
                pass

                    
# if __name__ == "__main__":
#     estoque = estoque_produto
#     livro_teste = livro()
#    livro_teste.criar_livro(estoque)
    # entrada_saida.obter_entrada_centralizada_float("teste",False)
main()