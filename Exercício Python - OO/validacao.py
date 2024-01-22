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
                    cadastro_nao_cancelado = False
                    return True
                case 2:
                    cadastro_nao_cancelado = False
                case 3:
                    verificar_edicao_livro(livro_em_cadastro, estoque)
        else:
            opcao_invalida = True

def verificar_edicao_livro(livro_em_cadastro, estoque):
    opcao_invalida = False
    operacao_rodando = True
    art = artes_ascii.titulo_livro_em_andamento
    while operacao_rodando:
        match entrada_saida.solicitar_menu_edicao(artes_ascii.titulo_livro_em_andamento,artes_ascii.menu_edicao_livro, opcao_invalida, 25):
            case 1:
                livro_em_cadastro.set_titulo(entrada_saida.solicitar_cadastro_livro_string(art,"o titulo", False,14))
            case 2:
                livro_em_cadastro.set_genero(entrada_saida.solicitar_categoria_livro())
            case 3:
                livro_em_cadastro.set_autoria(entrada_saida.solicitar_cadastro_livro_string(art,"a autoria", False,14))
            case 4:
                livro_em_cadastro.set_ano_lancamento(validar_ano_lancamento())
            case 5:
                livro_em_cadastro.set_quant_paginas(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade de páginas", False))
            case 6:
                livro_em_cadastro.set_classificacao_indicativa(validar_classificacao_indicativa())
            case 7:
                livro_em_cadastro.set_idioma(entrada_saida.solicitar_cadastro_livro_string(art,"o idioma", False,14))
            case 8:
                livro_em_cadastro.set_tiragem(entrada_saida.solicitar_cadastro_livro_int(art,"a tiragem", False))
            case 9:
                livro_em_cadastro.set_avaliacao_geral(validar_avaliacao_produtos(livro_em_cadastro))
            case 10:
                livro_em_cadastro.set_is_best_seller(valida_best_seller())
            case 11:
                livro_em_cadastro.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade disponível", False))
        operacao_rodando = False

    
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
                    verificar_edicao_midia(midia_em_cadastro, estoque)
                    
        else:
            opcao_invalida = True

def verificar_edicao_midia(midia_em_cadastro, estoque):
    opcao_invalida = False
    operacao_rodando = True
    art = artes_ascii.titulo_midia_em_andamento
    while operacao_rodando:
        match entrada_saida.solicitar_menu_edicao(artes_ascii.titulo_midia_em_andamento,artes_ascii.menu_edicao_midia, opcao_invalida, 25):
            case 1:
                midia_em_cadastro.set_titulo(entrada_saida.solicitar_cadastro_livro_string(art,"o titulo",False,14))
            case 2:
                midia_em_cadastro.set_categoria(entrada_saida.solicitar_categoria_midia())
            case 3:
                midia_em_cadastro.set_autoria(entrada_saida.solicitar_cadastro_livro_string(art,"a autoria",False,14))
            case 4:
                midia_em_cadastro.set_ano_lancamento(validar_ano_lancamento())
            case 5:
                midia_em_cadastro.set_classificacao_indicativa(validar_classificacao_indicativa())
            case 6:
                midia_em_cadastro.set_idioma(entrada_saida.solicitar_cadastro_livro_string(art,"o idioma",False,14))
            case 7:
                midia_em_cadastro.set_tiragem(entrada_saida.solicitar_cadastro_livro_int(art,"a tiragem",False))
            case 8:
                midia_em_cadastro.set_avaliacao_geral(validar_avaliacao_produtos(midia_em_cadastro))
            case 9:
                midia_em_cadastro.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade disponível",False,14))
        operacao_rodando = False

def confirmar_cadastro_revista(revista_em_cadastro, estoque):
    cadastro_nao_cancelado = True
    opcao_invalida = False
    while cadastro_nao_cancelado:
        entrada_saida.solicitar_confirmacao_revista(revista_em_cadastro)
        escolha = entrada_saida.solicitar_menu_sim_nao_editar(artes_ascii.menu_sim_não_editar,opcao_invalida,26)
        if escolha in (1,2,3):
            match escolha:
                case 1:
                    estoque.add_lista_produto(revista_em_cadastro)#Adiciona apenas uma amostra para exibir na lista de disponíveis
                    return True
                case 2:
                    cadastro_nao_cancelado = False
                case 3:
                    verificar_edicao_revista(revista_em_cadastro, estoque)
        else:
            opcao_invalida = True

def verificar_edicao_revista(revista_em_cadastro, estoque):
    opcao_invalida = False
    operacao_rodando = True
    art = artes_ascii.titulo_revista_em_andamento
    while operacao_rodando:
        match entrada_saida.solicitar_menu_edicao(artes_ascii.titulo_revista_em_andamento,artes_ascii.menu_edicao_revista, opcao_invalida, 25):
            case 1:
                revista_em_cadastro.set_titulo(entrada_saida.solicitar_cadastro_livro_string(art,"o titulo",False,14))
            case 2:
                revista_em_cadastro.set_volume(entrada_saida.solicitar_cadastro_livro_int(art,"o volume/edição",False))
            case 3:
                revista_em_cadastro.set_autoria(entrada_saida.solicitar_cadastro_livro_string(art,"a autoria",False,14))
            case 4:
                revista_em_cadastro.set_ano_lancamento(validar_ano_lancamento())
            case 5:
                revista_em_cadastro.set_quant_paginas(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade de páginas",False))
            case 6:
                revista_em_cadastro.set_classificacao_indicativa(validar_classificacao_indicativa())
            case 7:
                revista_em_cadastro.set_idioma(entrada_saida.solicitar_cadastro_livro_string(art,"o idioma",False,14))
            case 8:
                revista_em_cadastro.set_quantidade_disponivel(entrada_saida.solicitar_cadastro_livro_int(art,"a quantidade disponível",False))
        operacao_rodando = False

def verificar_edicao_cliente(cliente_em_cadastro):
    opcao_invalida = False
    operacao_rodando = True
    art = artes_ascii.titulo_cliente_em_andamento
    while operacao_rodando:
        match entrada_saida.solicitar_menu_edicao(artes_ascii.titulo_cliente_em_andamento, artes_ascii.menu_edicao_cliente,opcao_invalida, 18):
            case 1:
                cliente_em_cadastro.set_nome(entrada_saida.solicitar_cadastro_livro_string(art,"o nome",False,14))
            case 2:
                cliente_em_cadastro.set_rg(valida_rg_cliente())
            case 3:
                cliente_em_cadastro.set_telefone(valida_telefone_cliente())
            case 4:
                cliente_em_cadastro.set_endereco(entrada_saida.solicitar_cadastro_livro_string(art,"endereço",False,14))
        operacao_rodando = False
def confirmar_cadastro_jogos():
    print

def confirmar_cadastro_cliente(cliente_em_cadastro, lista_usuarios):
    cadastro_nao_cancelado = True
    opcao_invalida = False
    while cadastro_nao_cancelado:
        entrada_saida.solicitar_confirmacao_cliente(cliente_em_cadastro)
        escolha = entrada_saida.solicitar_menu_sim_nao_editar(artes_ascii.menu_sim_não_editar, opcao_invalida, 19)
        if escolha in (1,2,3):
            match escolha:
                case 1:
                    lista_usuarios.adicionar_cliente(cliente_em_cadastro)
                    cadastro_nao_cancelado = False
                    return True
                case 2:
                    cadastro_nao_cancelado = False
                case 3:
                    verificar_edicao_cliente(cliente_em_cadastro)
    
def confirmar_aluguel(cliente, produto, tempo_aluguel, estoque):
    if (entrada_saida.confirmar_aluguel(cliente, produto, tempo_aluguel)):
       produto.set_locatario(cliente)
       produto.set_tempo_aluguel(tempo_aluguel)
       estoque.add_lista_produto_alugado(produto)

def valida_rg_cliente():
    rg = ""
    opcao_invalida = False
    art = artes_ascii.titulo_cliente_em_andamento
    while True:
        rg = entrada_saida.solicitar_cadastro_livro_string(art,"o RG", opcao_invalida,14)
        if len(rg) != 7 or not rg.isdigit():
            opcao_invalida = True
        else:
            #rg_formatado = f"{rg[0]}.{'.'.join([rg[i:i+3] for i in range(1, 7, 3)])}"
            return rg

def valida_telefone_cliente():
    telefone = ""
    opcao_invalida = False
    art = artes_ascii.titulo_cliente_em_andamento
    while True:
        telefone = entrada_saida.solicitar_cadastro_livro_string(art,"telefone", opcao_invalida,14)
        if len(telefone) != 11 or not telefone.isdigit():
            opcao_invalida = True
        else:
            telefone_formatado = f"({telefone[:2]}) {telefone[2]} {telefone[3:7]}-{telefone[7:]}"
            return telefone_formatado
    
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

def validar_ano_lancamento(produto):
    match produto:
        case 1:
            art = artes_ascii.titulo_livro_em_andamento
        case 2:
            art = artes_ascii.titulo_midia_em_andamento
        case 3:
            art = artes_ascii.titulo_revista_em_andamento
    opcao_invalida = False
    while True:
        ano = entrada_saida.solicitar_ano_livro_int(art,"o ano de lançamento",opcao_invalida,14)
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

def validar_avaliacao_produtos(produto, livro):
    match produto:
        case 1:
            art = artes_ascii.titulo_livro_em_andamento
        case 2:
            art = artes_ascii.titulo_midia_em_andamento
        case 3:
            art = artes_ascii.titulo_revista_em_andamento
    opcao_invalida = False
    while True:
        avaliacao_geral = entrada_saida.solicitar_cadastro_livro_float(art,"a avaliação geral", opcao_invalida)
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



