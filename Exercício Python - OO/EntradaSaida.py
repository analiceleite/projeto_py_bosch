class EntradaSaida:
    def menuOpcoes():
        print("==============================\n")
        print("[1]- Cadastrar produtos\n[2]- Editar produtos\n[3]- Pesquisar produtos\n[4]- Sair")
        print("==============================\n")
        return int(input("Insira sua opção --> "))
    
    def menuCadastro():
        print("==============================\n")
        print("[1]- Livro\n[2]- Revistas\n[3]- CD's / DVD's\n[4]- Jogos de Tabuleiro\n[5]- Voltar")
        print("==============================\n")
        return int(input("Insira sua opção --> "))
    
    def solicitarCadastroLivro(msg):
        print("==============================\n")
        print("Insira ",msg,"do livro")
        print("==============================\n")
        return input("Insira sua opção --> ")