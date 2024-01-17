def retorno_opcao_inteiro():
    return int(input("Opção --> "))
def retorno_opcao_string():
    return int(input("---> "))


def menu_principal():
    print("[1]- Cadastrar\n[2]- Buscar\n[3]- Alugar\n[4]- Sair")
    retorno_opcao_inteiro

def menu_escolher_tipo_cadastro():
    print("[1]- Produto\n[2]- Cliente\n[3]- Voltar ao menu principal")

def menu_escolher_categoria(mensagem):
    print("[1]- Livro\n[2]- CD\n[3]- DVD\n[4]- Disco de vinil\n[5]- Blu-Ray\n[6]- Voltar ao menu "+mensagem)
    retorno_opcao_inteiro

def menu_cadastrar_dados(mensagem): #alugar/cadastro cliente
    print("Insira "+mensagem+":")
    retorno_opcao_string

def menu_buscar():
    print("[1]- Categoria\n[2]- Nome\n[3]- Voltar ao menu principal")
    retorno_opcao_inteiro

def menu_buscar_nome():
    return input("Insira o nome do item desejado: ")

def menu_escolher_tempo():
    print("[1]- 7 dias\n[2]- 14 dias\n[3]- 21 dias\n[4]- 28 dias")
    retorno_opcao_inteiro