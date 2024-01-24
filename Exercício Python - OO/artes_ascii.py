nome_biblioteca = """
██     ██  █████  ██████  ██████      ██      ██ ██████ 
 ██     ██ ██   ██ ██   ██ ██   ██     ██      ██ ██   ██ 
 ██  █  ██ ███████ ██████  ██████      ██      ██ ██████  
 ██ ███ ██ ██   ██ ██   ██ ██          ██      ██ ██   ██ 
  ███ ███  ██   ██ ██   ██ ██          ███████ ██ ██████  
                                                                                                                                                                                                   
"""
#separa_texto("--------------------------------------------------------")
opcao_invalida = "\n                   >> Opção Inválida <<                  "
titulo_principal = "                 >>> MENU PRINCIPAL <<<                 "
titulo_busca = "                   >>> MENU BUSCA <<<                   "

titulo_escolher_tipo_cadastro = "           >>> ESCOLHA O TIPO DE CADASTRO <<<           "
titulo_escolher_tipo_produto = "           >>> ESCOLHA O TIPO DO PRODUTO <<<            "
titulo_livro_em_andamento = "               >>> CADASTRANDO LIVRO <<<                "
titulo_livro_em_locacao = "                 >>> ALUGANDO LIVRO <<<                  "
titulo_midia_em_andamento = "            >>> CADASTRANDO MÍDIA DIGITAL <<<           "
titulo_revista_em_andamento = "              >>> CADASTRANDO REVISTA <<<               "
titulo_jogos_em_andamento = "               >>> CADASTRANDO JOGOS <<<                "
titulo_cliente_em_andamento = "              >>> CADASTRANDO CLIENTE <<<               "
titulo_confirmar_cadastro = "              >>> CONFIRMAR CADASTRO <<<                "
titulo_lista_geral = "            >>> LISTA GERAL DOS PRODUTOS <<<            "
titulo_editar_informacao = "\n          Selecione a informação a ser editada          "
titulo_best_seller = "\n              Este livro é um best seller?              "
titulo_emprestimo_confirmado = "               >>> ALUGUEL CONFIRMADO <<<               "


menu_principal_opcoes = """
 [1]- Cadastrar   
 [2]- Buscar      
 [3]- Alugar      
 [4]- Sair        
"""
menu_opcoes_cadastro = """
[1]- Produto   
[2]- Cliente    
             [3]- Voltar ao menu principal
"""

menu_escolher_tipo_produto = """
[1]- Livro     
  [2]- Mídia digital
[3]- Revistas  
[4]- Jogos     
                  [5]- Voltar para o menu principal
"""

menu_escolher_categoria_livro = """
[1]- Ação      
[2]- Aventura  
[3]- Comédia   
[4]- Romance   
[5]- Thriller  
"""
menu_escolher_categoria_midia = """
[1]- CD        
[2]- DVD       
[3]- Blu-Ray   
[4]- Fita VHS   
     [5]- Disco de Vinil  
"""

menu_busca = """
[1]- Exibir lista geral
     [2]- Voltar ao menu principal
"""
menu_busca_encontrado = """
[1]- Alugar
             [2]- Buscar outro produto
                 [3]- Voltar ao menu principal
"""
menu_sim_não_bestseller = """
 [1]- Sim 
 [2]- Não
"""
menu_sim_não_editar = """
 [1]- Sim 
 [2]- Não
       [3]- Editar    
"""
menu_edicao_livro = """
[1]- Título     
[2]- Gênero     
[3]- Autoria   
      [4]- Ano de lançamento
          [5]- Quantidade de páginas
             [6]- Classificação Indicativa
[7]- Idioma    
[8]- Tiragem   
[9]- Avaliação  
  [10]- Best Seller 
           [11]- Quantidade disponível
"""
menu_edicao_midia = """
[1]- Título     
[2]- Gênero     
[3]- Autoria   
      [4]- Ano de lançamento
             [5]- Classificação Indicativa
[6]- Idioma    
[7]- Tiragem   
[8]- Avaliação  
           [9]- Quantidade disponível
"""
menu_edicao_revista = """
[1]- Título     
[2]- Volume     
[3]- Autoria   
      [4]- Ano de lançamento
          [5]- Quantidade de páginas
             [6]- Classificação Indicativa
[7]- Idioma     
           [8]- Quantidade disponível
"""
menu_edicao_cliente = """
  [1]- Nome
[2]- RG
     [3]- Telefone
     [4]- Endereço
"""
menu_tempo_aluguel = """
[1]- 7 dias
[2]- 14 dias
[3]- 21 dias
[4]- 28 dias
"""

def confirmacao_livro(livro):
    detalhes_livro = (
    f"\nTítulo: {livro.get_titulo()}\n"
    f"Gênero: {livro.get_genero()}\n"
    f"Autoria: {livro.get_autoria()}\n"
    f"Ano lançamento: {livro.get_ano_lancamento()}\n"
    f"Quantidade de páginas: {livro.get_quant_paginas():,} pgs.\n"
    f"Classificação indicativa: {livro.get_classificacao_indicativa()}+\n"
    f"Idioma: {livro.get_idioma()}\n"
    f"Tiragem: {livro.get_tiragem():,} cópias\n"
    f"Avaliação: {livro.get_avaliacao_geral()}\n"
    f"Best Seller: {livro.get_is_best_seller()}\n"
    f"Quantidade disponível: {livro.get_quantidade_disponivel():,}"
    )
    return detalhes_livro

def confirmacao_midia(midia):
    detalhes_midia = (
    f"\nTítulo: {midia.get_titulo()}\n"
    f"Gênero: {midia.get_categoria()}\n"
    f"Autoria: {midia.get_autoria()}\n"
    f"Ano lançamento: {midia.get_ano_lancamento()}\n"
    f"Tempo duração: {midia.get_tempo_duracao()} minuto(s)\n"
    f"Classificação indicativa: {midia.get_classificacao_indicativa()}+\n"
    f"Idioma: {midia.get_idioma()}\n"
    f"Tiragem: {midia.get_tiragem():,} cópia(s)\n"
    f"Avaliação: {midia.get_avaliacao_geral()}\n"
    f"Quantidade disponível: {midia.get_quantidade_disponivel():,}"
    )
    return detalhes_midia

def confirmacao_revista(revista):
    detalhes_revista = (
    f"\nTítulo: {revista.get_titulo()}\n"
    f"Volume/Edição: {revista.get_volume()}\n"
    f"Autoria: {revista.get_autoria()}\n"
    f"Ano lançamento: {revista.get_ano_lancamento()}\n"
    f"Quantidade de páginas: {revista.get_quant_paginas():,} pgs.\n"
    f"Classificação indicativa: {revista.get_classificacao_indicativa()}+\n"
    f"Idioma: {revista.get_idioma()}\n"
    f"Quantidade disponível: {revista.get_quantidade_disponivel():,}"
    )
    return detalhes_revista

def confirmacao_cliente(cliente):
    detalhes_cliente = (
    f"\nNome: {cliente.get_nome()}\n"
    f"{cliente.get_rg()[0]}.{'.'.join([cliente.get_rg()[i:i+3] for i in range(1, 7, 3)])}\n"
    #f"RG: {cliente.get_rg()}\n"
    f"Telefone: {cliente.get_telefone()}\n"
    f"Endereço: {cliente.get_endereco()}"
    )
    return detalhes_cliente

def confirmacao_aluguel(produto, cliente, data_retirada, data_devolutiva):
  detalhes_aluguel = (
  f"\nProduto: {produto.get_titulo()}\n"
  f"Locatário: {cliente.get_nome()}\n"
  f"Data de retirada: {data_retirada}\n"
  f"Data de devolutiva: {data_devolutiva}\n"
  )
  return detalhes_aluguel