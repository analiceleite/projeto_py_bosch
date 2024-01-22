import entrada_saida
from estoque_produto import estoque_produto
from gestao_clientes import gestao_clientes
import random
import artes_ascii

def confirmar_cadastro_livro(livro_em_cadastro,estoque):
    cadastro_nao_cancelado = True
    opcao_invalida = False
    while cadastro_nao_cancelado:
        entrada_saida.solicitar_confirmacao_livro(livro_em_cadastro)
        escolha = entrada_saida.solicitar_menu_sim_nao_editar(artes_ascii.menu_sim_não_editar,opcao_invalida,26)
        if escolha in (1,2,3):
            match escolha:
                case 1:
                    estoque.add_lista_produto(livro_em_cadastro)#Adiciona apenas uma amostra para exibir na lista de disponíveis
                    return True
                case 2:
                    cadastro_nao_cancelado = False
                case 3:
                    return verificar_edicao_livro(livro_em_cadastro, estoque)
                    
        else:
            opcao_invalida = True

def verificar_edicao_livro(livro_em_cadastro, estoque):
    opcao_invalida = False
    i = 0
    while True:
        match entrada_saida.solicitar_menu_edicao(artes_ascii.titulo_livro_em_andamento,artes_ascii.menu_edicao_livro, opcao_invalida, 25):
            case 1:
                livro_em_cadastro.set_titulo(entrada_saida.solicitar_cadastro_livro_string("o titulo"))                
            case 2:
                livro_em_cadastro.set_genero(entrada_saida.solicitar_categoria_livro())
            case 3:
                livro_em_cadastro.set_autoria(entrada_saida.solicitar_cadastro_livro_string("a autoria"))
            case 4:
                livro_em_cadastro.set_ano_lancamento(validar_ano_lancamento())
            case 5:
                livro_em_cadastro.set_quant_paginas(entrada_saida.solicitar_cadastro_livro_int("a quantidade de páginas"))
            case 6:
                livro_em_cadastro.set_classificacao_indicativa(validar_classificacao_indicativa())
            case 7:
                livro_em_cadastro.set_idioma(entrada_saida.solicitar_cadastro_livro_string("o idioma"))
            case 8:
                livro_em_cadastro.set_tiragem(entrada_saida.solicitar_cadastro_livro_int("a tiragem"))
            case 9:
                livro_em_cadastro.set_avaliacao_geral(validar_avaliacao_produtos(livro_em_cadastro))
            case 10:
                livro_em_cadastro.set_is_best_seller(valida_best_seller())
            case 11:
                livro_em_cadastro.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int("a quantidade disponível"))
        match confirmar_cadastro_livro(livro_em_cadastro, estoque):
            case 1:
                return livro_em_cadastro
            case 2:
                break
    
def confirmar_cadastro_midia(midia_em_cadastro, estoque):
    cadastro_nao_cancelado = True
    opcao_invalida = False
    while cadastro_nao_cancelado:
        entrada_saida.solicitar_confirmacao_midia(midia_em_cadastro)
        escolha = entrada_saida.solicitar_menu_sim_nao_editar(artes_ascii.menu_sim_não_editar,opcao_invalida,25)
        if escolha in (1,2,3):
            match escolha:
                case 1:
                    estoque.add_lista_produto(midia_em_cadastro)#Adiciona apenas uma amostra para exibir na lista de disponíveis
                    return True
                case 2:
                    cadastro_nao_cancelado = False
                case 3:
                    return verificar_edicao_midia(midia_em_cadastro, estoque)
                    
        else:
            opcao_invalida = True

def verificar_edicao_midia(midia_em_cadastro, estoque):
    opcao_invalida = False
    i = 0
    while True:
        match entrada_saida.solicitar_menu_edicao(artes_ascii.titulo_midia_em_andamento,artes_ascii.menu_edicao_midia, opcao_invalida, 25):
            case 1:
                midia_em_cadastro.set_titulo(entrada_saida.solicitar_cadastro_livro_string("o titulo"))                
            case 2:
                midia_em_cadastro.set_categoria(entrada_saida.solicitar_categoria_midia())
            case 3:
                midia_em_cadastro.set_autoria(entrada_saida.solicitar_cadastro_livro_string("a autoria"))
            case 4:
                midia_em_cadastro.set_ano_lancamento(validar_ano_lancamento())
            case 5:
                midia_em_cadastro.set_classificacao_indicativa(validar_classificacao_indicativa())
            case 6:
                midia_em_cadastro.set_idioma(entrada_saida.solicitar_cadastro_livro_string("o idioma"))
            case 7:
                midia_em_cadastro.set_tiragem(entrada_saida.solicitar_cadastro_livro_int("a tiragem"))
            case 8:
                midia_em_cadastro.set_avaliacao_geral(validar_avaliacao_produtos(midia_em_cadastro))
            case 9:
                midia_em_cadastro.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int("a quantidade disponível"))
        match confirmar_cadastro_midia(midia_em_cadastro, estoque):
            case 1:
                return midia_em_cadastro
            case 2:
                break


def confirmar_cadastro_revista(revista_em_cadastro, estoque):
    if(entrada_saida.solicitar_confirmacao_revista(revista_em_cadastro)):
        estoque.add_lista_produto(revista_em_cadastro)#Adiciona apenas uma amostra no estoque
        return True
    else:
        entrada_saida.imprime_cadastro_cancelado()

def confirmar_cadastro_jogos():
    print

def confirmar_cadastro_cliente(cliente_em_cadastro, lista_usuarios):
    if (entrada_saida.solicitar_confirmacao_cadastro_cliente(cliente_em_cadastro)):
        lista_usuarios.adicionar_cliente(cliente_em_cadastro)
    else:
        entrada_saida.imprime_cadastro_cancelado()
    
def confirmar_aluguel(cliente, produto, tempo_aluguel, estoque):
    if (entrada_saida.confirmar_aluguel(cliente, produto, tempo_aluguel)):
       produto.set_locatario(cliente)
       produto.set_tempo_aluguel(tempo_aluguel)
       estoque.add_lista_produto_alugado(produto)


def confirmar_tempo_aluguel():
    match entrada_saida.solicitar_tempo_aluguel():
        case 1:
            return 7
        case 2:
            return 14
        case 3:
            return 21
        case 4:
            return 28
        
def validar_exibicao_busca(produto):
    if(produto.get_tipo() == "Livro"):
        entrada_saida.exibir_livro_pesquisado(produto)
    elif(produto.get_tipo() == "Revista"):
        entrada_saida.exibir_revista_pesquisada(produto)
    else:
        entrada_saida.exibir_midia_digital_pesquisada(produto)

def validar_ano_lancamento():
    opcao_invalida = False
    while True:
        ano = entrada_saida.solicitar_ano_livro_int("o ano de lançamento",opcao_invalida)
        if ano > 1000 and ano <= 2024:
            return ano
        else:
            opcao_invalida = True

def validar_classificacao_indicativa():
    opcao_invalida = False
    entrada = 5
    while True:
        classificacao_indicativa = entrada_saida.solicitar_classificacao_indicativa_int("a classificação indicativa", opcao_invalida)
        if classificacao_indicativa.isdigit():
            entrada = int(classificacao_indicativa)
            if entrada == 0:
                return "Livre"
            elif entrada >= 18:
                return 18
            else:
                return entrada
        elif classificacao_indicativa.lower() == "l":
            return "Livre"
        opcao_invalida = True

def validar_avaliacao_produtos(livro):
    opcao_invalida = False
    while True:
        avaliacao_geral = entrada_saida.solicitar_cadastro_livro_float("a avaliação geral", opcao_invalida)
        if avaliacao_geral > 5 or avaliacao_geral < 0:
            opcao_invalida = True
        else:
            break
    quantidade_votos = random.randint(1,livro.get_tiragem())
    livro.set_quantidade_votos(quantidade_votos)
    return avaliacao_geral

def valida_best_seller():
    opcao_invalida = False
    while True:
        match entrada_saida.solicitar_menu_sim_nao(artes_ascii.menu_sim_não_bestseller,opcao_invalida):
            case 1:
                return "Sim"
            case 2:
                return "Não"
            case _:
                opcao_invalida = True

def adicionar_avaliacao():
    # avaliacao_geral = ((avaliacao_geral * quantidade_votos) + nova_avaliacao) / (self.quantidade_votos + 1)
    # quantidade_votos += 1
    pass



