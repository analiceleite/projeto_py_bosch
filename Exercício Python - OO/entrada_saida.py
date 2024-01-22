from livro import livro
from midia_digital import midia_digital
from revista import revista
import os
import artes_ascii
import shutil
#Coleta largura do terminal para utilizar na centralização de texto
largura_tela = os.get_terminal_size().columns




def obter_entrada_centralizada_string(mensagem,linha):
    largura_tela, _ = shutil.get_terminal_size()
    coluna_central = (largura_tela - len(mensagem)) // 2
    print(f"\033[{linha};{coluna_central}H{mensagem}", end="")
    coluna_input = coluna_central + len(mensagem)
    input_posicionado = input(f"\033[{linha};{coluna_input-5}H")
    if (input_posicionado.isalnum):
        return input_posicionado
    return False

def obter_entrada_centralizada_int(mensagem,linha):
    largura_tela, _ = shutil.get_terminal_size()
    coluna_central = (largura_tela - len(mensagem)) // 2
    print(f"\033[{linha};{coluna_central}H{mensagem}", end="")
    coluna_input = coluna_central + len(mensagem)
    input_posicionado = input(f"\033[{linha};{coluna_input-5}H")
    if (input_posicionado.isdigit()):
        return int(input_posicionado)
    return False

def obter_entrada_centralizada_float(mensagem,linha):
    largura_tela, _ = shutil.get_terminal_size()
    coluna_central = (largura_tela - len(mensagem)) // 2
    print(f"\033[{linha};{coluna_central}H{mensagem}", end="")
    coluna_input = coluna_central + len(mensagem)
    input_posicionado = input(f"\033[{linha};{coluna_input-5}H")
    
    # if(input_posicionado.isdigit()):
    #     input_replace = input_posicionado.replace(",",".")
    #     input_float = float(input_replace)
    #     return input_float
    # else:
    try:
        input_replace = input_posicionado.replace(",",".")
        input_float = float(input_replace)
        return input_float
    except:
        return False

    # if (not input_posicionado.isdigit()):
    #     return False
    # input_replace = input_posicionado.replace(",",".")
    # input_float = float(input_replace)
    # if (input_float):
    #     return input_float
    # return False
    


#Limpatela com cls
def limpa_tela():
    os.system("cls")
    #print("\n"*os.get_terminal_size().lines) //Comando antigo que coleta o tamanho do terminal e printa o mesmo com \n

def separa_texto(texto):
    linhas = texto.split('\n')
    for linha in linhas:
        #print('\033[33m'+centralizar_texto(linha, largura_tela)+'\033[0;0m')
        print('\033[33m'+linha.center(largura_tela)+'\033[0;0m')
        

def separa_confirmacao_livro(texto):
    linhas = texto.split("\n")
    for linha in linhas:
        print('\033[33m'+centralizar_texto(linha, largura_tela)+'\033[0;0m')
    return True

def centraliza_titulo_menu(texto):
    linhas = texto.split('\n')
    for linha in linhas:
        print('\033[33m'+'\033[1m'+linha.center(largura_tela)+'\033[0;0m')

def centraliza_opcao_invalida(texto):
    linhas = texto.split('\n')
    for linha in linhas:
        print('\033[33m'+'\033[31m'+linha.center(largura_tela)+'\033[0;0m')

def centraliza_insersor(texto):
    linhas = texto.split()
    for linha in linhas:
        print('\033[33m'+'\033[31m'+linha.center(largura_tela)+'\033[0;0m')

def imprime_menu(texto):
    linhas = texto.split('\n')
    for linha in linhas:
        print('\033[33m',centralizar_texto(linha, largura_tela),'\033[0;0m')

#-------------------------------------------------#
        #Método que centraliza texto
def centralizar_texto(texto, largura_tela):
    espacos_totais = largura_tela - len(texto)
    margem_esquerda = espacos_totais // 2
    return ' '*margem_esquerda+texto
        #Centraliza o texto e imprime no terminal
#-------------------------------------------------#


def retorno_opcao_inteiro():
    return int(input("---> "))
def retorno_opcao_float():
    return float(input("Opção --> "))
def retorno_opcao_string():
    centraliza_titulo_menu(" ")
    return input("---> ")

## ------- MENUS ------- ## 
#Menu Principal
def menu_principal(): #Editar formato do input do usuário
    opcaoInvalida = False
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_principal)
        if (opcaoInvalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
        imprime_menu(artes_ascii.menu_principal_opcoes) ## Imprime menu de opções
        opcao_escolha = retorno_opcao_inteiro()
        if (opcao_escolha in (1,2,3,4)): ## Verifica input com quantidade de opções disponíveis
            return opcao_escolha
        else:
            opcaoInvalida = True

#Menu de opções para tipo de cadastro
def menu_escolher_tipo_cadastro():
    opcaoInvalida = False
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_escolher_tipo_cadastro)
        if (opcaoInvalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
        imprime_menu(artes_ascii.menu_opcoes_cadastro)
        opcao_escolha = retorno_opcao_inteiro()
        if (opcao_escolha in (1,2,3)):
            return opcao_escolha
        else:
            opcaoInvalida = True

#Menu de opções para tipo de cadastro de produto
def menu_escolher_tipo_produto():
    opcaoInvalida = False
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_escolher_tipo_produto)
        if (opcaoInvalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
        imprime_menu(artes_ascii.menu_escolher_tipo_produto)
        opcao_escolha = retorno_opcao_inteiro()
        if (opcao_escolha in (1,2,3,4,5)):
            return opcao_escolha
        else:
            opcaoInvalida = True

def menu_item_pesquisado():
    print("[1]- Alugar\n[2]- Buscar outro produto\n[3]- Voltar ao menu principal")
    return retorno_opcao_inteiro()

def solicitar_rg_aluguel(): #Solicita RG do cliente no momento do aluguel do produto
    print("Insira o RG do cliente: ")
    return retorno_opcao_string()

## solicitar_tempo_aluguel
#def solicitar_confirmacao_aluguel(produto, cliente):
#    print("D")


def menu_escolher_categoria(mensagem):
    print("[1]- Livro\n[2]- CD\n[3]- DVD\n[4]- Disco de vinil\n[5]- Blu-Ray\n[6]- Voltar ao menu "+mensagem)
    return retorno_opcao_inteiro()
#Menus Jogos

#Menus Mídia digital

## ------- SOLICITAÇÕES ------- ## 
def solicitar_cadastro_livro_string(mensagem):
    opcaoInvalida = False
    linha = 13
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        if(opcaoInvalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 14
        centraliza_titulo_menu("\nInsira "+mensagem)
        entrada = obter_entrada_centralizada_string("\033[33m"+"---> ",linha) 
        if (entrada):
            return entrada
        opcaoInvalida = True

def solicitar_cadastro_livro_int(mensagem):
    opcaoInvalida = False
    linha = 13
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        if(opcaoInvalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 14
        centraliza_titulo_menu("\nInsira "+mensagem)
        entrada = obter_entrada_centralizada_int("\033[33m"+"---> ",linha) 
        if (entrada):
            return entrada
        opcaoInvalida = True

def solicitar_cadastro_livro_float(mensagem, opcao_invalida):
    linha = 13
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        if(opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 14
        centraliza_titulo_menu("\nInsira "+mensagem)
        entrada = obter_entrada_centralizada_float("\033[33m"+"---> ",linha) 
        if (entrada):
            return entrada
        opcao_invalida = True

def solicitar_categoria_livro():
    opcao_invalida = False
    linha = 20
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        if (opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 21
        centraliza_titulo_menu("\nEscolha o gênero do livro")
        imprime_menu(artes_ascii.menu_escolher_categoria_livro)
        match obter_entrada_centralizada_int("\033[33m"+"---> ",linha):
            case 1:
                return "Ação"
            case 2:
                return "Aventura"
            case 3:
                return "Comédia"
            case 4:
                return "Romance"
            case 5:
                return "Thriller"
            case _:
                opcao_invalida = True
                
def solicitar_categoria_midia():
    opcao_invalida = False
    linha = 20
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_midia_em_andamento)
        if (opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 21
        centraliza_titulo_menu("\nEscolha a categoria da mídia digital")
        imprime_menu(artes_ascii.menu_escolher_categoria_midia)
        match obter_entrada_centralizada_int("\033[33m"+"---> ",linha):
            case 1:
                return "CD"
            case 2:
                return "DVD"
            case 3:
                return "Blu-Ray"
            case 4:
                return "Fita VHS"
            case 5:
                return "Disco de Vinil"
            case _:
                opcao_invalida = True

def solicitar_ano_livro_int(mensagem,opcao_invalida):
    linha = 13
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        if(opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 14
        centraliza_titulo_menu("\nInsira "+mensagem)
        entrada = obter_entrada_centralizada_int("\033[33m"+"---> ",linha) 
        if (entrada):
            return entrada
        opcao_invalida = True

def solicitar_classificacao_indicativa_int(mensagem,opcao_invalida):
    linha = 13
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        if(opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 14
        centraliza_titulo_menu("\nInsira "+mensagem)
        entrada = obter_entrada_centralizada_string("\033[33m"+"---> ",linha) 
        if (entrada):
            return entrada
        opcao_invalida = True

def solicitar_menu_sim_nao(mensagem, opcao_invalida):
    linha = 15
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(artes_ascii.titulo_livro_em_andamento)
        centraliza_titulo_menu(artes_ascii.titulo_best_seller)
        if(opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha = 17
        centraliza_titulo_menu(mensagem)
        entrada = obter_entrada_centralizada_int("\033[33m"+"---> ",linha) 
        if (entrada):
            return entrada
        opcao_invalida = True

def solicitar_menu_sim_nao_editar(mensagem, opcao_invalida,linha):
    while True:
        if(opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha+=1
        centraliza_titulo_menu(mensagem)
        entrada = obter_entrada_centralizada_int("\033[33m"+"---> ",linha) 
        linha-=1
        return entrada
        #opcao_invalida = True

def solicitar_menu_edicao(menu, mensagem, opcao_invalida, linha):
    while True:
        limpa_tela()
        separa_texto(artes_ascii.nome_biblioteca)
        centraliza_titulo_menu(menu)
        centraliza_titulo_menu(artes_ascii.titulo_editar_informacao)
        if(opcao_invalida):
            centraliza_opcao_invalida(artes_ascii.opcao_invalida)
            linha += 1
        centraliza_titulo_menu(mensagem)
        entrada = obter_entrada_centralizada_int("\033[33m"+"---> ",linha)
        if (entrada):
            return entrada
        opcao_invalida = True

def solicitar_cadastro_produto_geral(mensagem): #alugar/cadastro cliente/produtos
    centraliza_titulo_menu("\nInsira o "+mensagem+":")
    return retorno_opcao_string()


def solicitar_quantidade_disponivel():
    print("Insira a quantidade disponível:")
    return retorno_opcao_inteiro()

def solicitar_dados_cliente(mensagem):
    print("Insira o "+mensagem+" do cliente:")
    return retorno_opcao_string()

def solicitar_tempo_aluguel():
    print("Por quanto tempo será alugado:\n[1]- 7 dias\n[2]- 14 dias\n[3]- 21 dias\n[4]- 28 dias")
    return retorno_opcao_inteiro()

def confirmar_aluguel(cliente, produto, tempo_aluguel):
    print("Produto:",produto.get_titulo(),"\nLocatário:",cliente.get_nome(),"\nTempo para devolução:",tempo_aluguel,"\n\nDeseja confirmar o aluguel?\n[1]- Sim\n[2]- Não")
    match retorno_opcao_inteiro():
        case 1:
            return True
        case 2:
            return False
    

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
                return retorno_opcao_inteiro()#retorno float
            except:
                opcaoValida = True
                print("Opção inválida")

def solicitar_id_buscar(): 
    opcaoValida = True
    while opcaoValida:
        try:
            print("Insira o ID do produto: ")
            return retorno_opcao_inteiro()
        except:
                opcaoValida = True
                print("Opção inválida")



def menu_solicitar_categoria_midia():
    print("Escolha a categoria da mídia:\n[1]- CD\n[2]- DVD\n[3]- Blu-Ray\n[4]- Fita\n[5]- Disco de vinil\n[6]- Voltar ao menu principal")
    match retorno_opcao_inteiro():
        case 1:
            return "CD"
        case 2:
            return "DVD"
        case 3:
            return "Blu-Ray"
        case 4:
            return "Fita"
        case 5:
            return "Disco de vinil"
        case 6:
            return "VERIFICAR VOLTA AO MENU"
 
def menu_buscar():
    print("[1]- Exibir lista geral\n[2]- Voltar ao menu principal")
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

def bool_menu_confirmacao():
    opcaoInvalida = True
    teste = False
    while opcaoInvalida:
        if(teste):
            print("Opção inválida")
        print("\nDeseja confirmar o cadastro?\n[1]- Sim\n[2]- Não")
        opcao = retorno_opcao_inteiro()
        if(opcao == 1):
            return True
        elif(opcao == 2):
            return False
        else:
            opcaoInvalida = True
            teste = True

def imprime_cadastro_cancelado():
    print("O cadastro foi cancelado")

def solicitar_confirmacao_cadastro_cliente(cliente_em_cadastro):
    print("Nome:",cliente_em_cadastro.get_nome(),"\nRG:",cliente_em_cadastro.get_rg(),"\nTelefone:",cliente_em_cadastro.get_telefone(),"\nEndereço",cliente_em_cadastro.get_endereco())
    return bool_menu_confirmacao()

def solicitar_confirmacao_livro(livro_em_cadastro):
    limpa_tela()
    separa_texto(artes_ascii.nome_biblioteca)
    centraliza_titulo_menu(artes_ascii.titulo_confirmar_cadastro)
    detalhes_livro = artes_ascii.confirmacao_livro(livro_em_cadastro)
    separa_confirmacao_livro(detalhes_livro)
    

def solicitar_confirmacao_midia(midia_em_cadastro):
    limpa_tela()
    separa_texto(artes_ascii.nome_biblioteca)
    centraliza_titulo_menu(artes_ascii.titulo_confirmar_cadastro)
    detalhes_midia = artes_ascii.confirmacao_midia(midia_em_cadastro)
    separa_confirmacao_livro(detalhes_midia)

def solicitar_confirmacao_revista(revista_em_cadastro):
    print("Título:",revista_em_cadastro.get_titulo(),"\nVolume/Edição:",revista_em_cadastro.get_volume(),"\nAutoria:",revista_em_cadastro.get_autoria(),"\nAno lançamento:",revista_em_cadastro.get_ano_lancamento(),"\nClassificação indicativa:",revista_em_cadastro.get_classificacao_indicativa(),"+\nIdioma:",revista_em_cadastro.get_idioma())
    return bool_menu_confirmacao()

def exibir_livro_pesquisado(livro_pesquisado):
    print("Título:",livro_pesquisado.get_titulo(),"\nGênero:",livro_pesquisado.get_genero(),"\nAutoria:",livro_pesquisado.get_autoria(),"\nAno lançamento:",livro_pesquisado.get_ano_lancamento(),"\nQuantidade de páginas:",livro_pesquisado.get_quant_paginas(),"pgs.\nClassificação indicativa:",livro_pesquisado.get_classificacao_indicativa(),"+\nIdioma:",livro_pesquisado.get_idioma()+"\nTiragem:",livro_pesquisado.get_tiragem(),"\nAvaliação:",livro_pesquisado.get_avaliacao_geral(),"\nBest Seller:",livro_pesquisado.get_is_best_seller())

def exibir_midia_digital_pesquisada(midia_digital):
    print("Título:",midia_digital.get_titulo(),"\nCategoria:",midia_digital.get_categoria(),"\nAutoria:",midia_digital.get_autoria(),"\nAno lançamento:",midia_digital.get_ano_lancamento(),"\nClassificação indicativa:",midia_digital.get_classificacao_indicativa(),"+\nIdioma:",midia_digital.get_idioma()+"\nTiragem:",midia_digital.get_tiragem(),"\nAvaliação:",midia_digital.get_avaliacao_geral())

def exibir_revista_pesquisada(revista_pesquisada):
    print("Título:",revista_pesquisada.get_titulo(),"\nVolume/Edição:",revista_pesquisada.get_volume(),"\nAutoria:",revista_pesquisada.get_autoria(),"\nAno lançamento:",revista_pesquisada.get_ano_lancamento(),"\nClassificação indicativa:",revista_pesquisada.get_classificacao_indicativa(),"+\nIdioma:",revista_pesquisada.get_idioma())