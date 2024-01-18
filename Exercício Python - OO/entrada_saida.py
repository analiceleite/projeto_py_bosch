from livro import livro
from midia_digital import midia_digital
from revista import revista

def retorno_opcao_inteiro():
    return int(input("---> "))
def retorno_opcao_float():
    return float(input("Opção --> "))
def retorno_opcao_string():
    return input("---> ")

#Menu Principal
def menu_principal():
    print("[1]- Cadastrar\n[2]- Buscar\n[3]- Alugar\n[4]- Sair")
    return retorno_opcao_inteiro()

def menu_escolher_tipo_cadastro():
    print("[1]- Produto\n[2]- Cliente\n[3]- Voltar ao menu principal")
    return retorno_opcao_inteiro()

def menu_escolher_categoria(mensagem):
    print("[1]- Livro\n[2]- CD\n[3]- DVD\n[4]- Disco de vinil\n[5]- Blu-Ray\n[6]- Voltar ao menu "+mensagem)
    return retorno_opcao_inteiro()

#Menus Jogos
#-----------

#Menus Mídia digital
def menu_escolher_tipo_produto():
    print("[1]- Livro\n[2]- Mídia digital\n[3]- Revistas\n[4]- Jogos\n[5]- Voltar para o menu principal")
    return retorno_opcao_inteiro()

def menu_escolher_midia_fisica():
    print("[1]- CD\n[2]- DVD\n[3]- Blu-ray\n[4]- Disco de vinil\n[5]- Fita\n[6]- Mais de uma categoria disponível\n[7]- Voltar ao menu principal")
    return retorno_opcao_inteiro()

def solicitar_cadastro_produto_geral(mensagem): #alugar/cadastro cliente/produtos
    print("Insira "+mensagem+":")
    return retorno_opcao_string()

def solicitar_cadastro_produto_geral_int(mensagem): #alugar/cadastro cliente/produtos
        opcaoValida = True
        while opcaoValida:
            try:
                print("Insira "+mensagem+":")
                return retorno_opcao_inteiro()
            except:
                opcaoValida = True
                print("Opção inválida")

def solicitar_cadastro_produto_geral_float(mensagem): #alugar/cadastro cliente/produtos
        opcaoValida = True
        while opcaoValida:
            try:
                print("Insira "+mensagem+":")
                return retorno_opcao_inteiro()
            except:
                opcaoValida = True
                print("Opção inválida")

def menu_solicitar_categoria_livro():
    print("[1]- Ação\n[2]- Aventura\n[3]- Comédia\n[4]- Romance\n[5]- Thriller\n[6]- Voltar ao menu principal")
    return retorno_opcao_inteiro

def menu_buscar():
    print("[1]- Categoria\n[2]- Nome\n[3]- Voltar ao menu principal")
    return retorno_opcao_inteiro()

def menu_buscar_nome():
    return input("Insira o nome do item desejado: ")

def menu_escolher_tempo():
    print("[1]- 7 dias\n[2]- 14 dias\n[3]- 21 dias\n[4]- 28 dias")
    return retorno_opcao_inteiro()

#Solicita dados para cadastro de produtos

def solicitar_best_seller():
    print("Este livro é um best seller?\n[1]- Sim\n[2]- Não")
    return retorno_opcao_inteiro()

def solicitar_confirmacao_livro(livro_em_cadastro):
    print("Título:",livro_em_cadastro.get_titulo(),"\nGênero:",livro_em_cadastro.get_genero(),"\nAutoria:",livro_em_cadastro.get_autoria(),"\nAno lançamento:",livro_em_cadastro.get_ano_lancamento(),"\nQuantidade de páginas:",livro_em_cadastro.get_quant_paginas(),"pgs.\nClassificação indicativa:",livro_em_cadastro.get_classificacao_indicativa(),"+\nIdioma:",livro_em_cadastro.get_idioma()+"\nTiragem:",livro_em_cadastro.get_tiragem(),"\nAvaliação:",livro_em_cadastro.get_avaliacao_geral(),"\nBest Seller:",livro_em_cadastro.get_is_best_seller())