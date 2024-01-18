import entrada_saida
from estoque_produto import estoque_produto
#from main import main

def confirmar_cadastro_livro(livro_em_cadastro,estoque):
    is_confirmado = entrada_saida.solicitar_confirmacao_livro(livro_em_cadastro)
    if(is_confirmado):
        estoque.add_lista_produto(livro_em_cadastro)
    else:
        entrada_saida.imprime_cadastro_cancelado()

def confirmar_cadastro_midia(midia_em_cadastro, estoque):
    is_confirmado = entrada_saida.solicitar_confirmacao_midia(midia_em_cadastro)
    if(is_confirmado):
        estoque.add_lista_produto(midia_em_cadastro)
    else:
        entrada_saida.imprime_cadastro_cancelado()

def confirmar_cadastro_revista(revista_em_cadastro, estoque):
    is_confirmado = entrada_saida.solicitar_confirmacao_revista(revista_em_cadastro)
    if(is_confirmado):
        estoque.add_lista_produto(revista_em_cadastro)
    else:
        entrada_saida.imprime_cadastro_cancelado()