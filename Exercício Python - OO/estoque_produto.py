from item_biblioteca import *
from livro import *
from revista import *
from midia_digital import *
from gestao_clientes import *

class estoque_produto:
    def __init__(self):
        self.__lista_produto = []
        self.__lista_produto_alugado = []
        self.__lista_livro = []


        self.__lista_midia_digital = []
        self.__lista_revista = []

    def get_lista_livro(self):
        return self.__lista_livro
    def set_lista_livro(self, value):
        self.__lista_livro = value
    def get_lista_produto_alugado(self):
        return self.__lista_produto_alugado
    def set_lista_produto_alugado(self, value):
        self.__lista_produto_alugado = value
    def get_lista_produto(self):
        return self.__lista_produto
    def set_lista_produto(self, value):
        self.__lista_produto = value

    def add_lista_produto(self, produto_em_cadastro):
        self.__lista_produto.append(produto_em_cadastro)

    def mostrar_lista_produto(self):
        for produto in self.__lista_produto:
            print(produto.get_titulo())

    def add_lista_produto_alugado(self, produto):
        self.__lista_produto_alugado.append(produto)
        for p in self.get_lista_produto_alugado():
            print(p.get_locatario())
            print(p.get_tempo_aluguel())
            print(p.get_titulo())
            exit()
            #print(produto.get_dono().get_nome())# Método para acessar o nome do dono
        
    def add_lista_livro(livro,self):
        print(livro)
        livro.__lista_livro.append(livro)
        print("adicionou")

    def opcao_menu_busca(quant_estoque):
        return entrada_saida.menu_buscar(quant_estoque,False)
    
    def exibir_lista_geral(estoque,lista_usuarios):
        operacao_nao_cancelada = True
        while operacao_nao_cancelada:
            produto_em_busca = estoque.exibir_lista_produto()
            produto_localizado = estoque.buscar_produto(produto_em_busca)
            if (produto_localizado):
                match entrada_saida.solicitar_menu_sim_nao_editar(artes_ascii.menu_busca_encontrado, False, 26):
                    case 1: #Alugar
                        estoque.alugar_produto(produto_localizado,lista_usuarios,estoque)
                        break
                    case 2: #Buscar outro produto
                        pass
                    case 3: #Voltar ao menu principal
                        break
        

    def atribuir_id(self):
        id = 1
        for produto in self.__lista_produto:
            if (produto.get_id() >= id):
                id = produto.get_id() + 1
        return id

    def exibir_lista_produto(self):
        cont = 1
        lista = ""
        opcao_invalida = False
        while True:
            entrada_saida.limpa_tela()
            entrada_saida.separa_texto(artes_ascii.nome_biblioteca)
            for produto in self.__lista_produto:
                lista += str(produto.get_id()) + "- " + str(produto.get_titulo()) + " ("+str(produto.get_tipo())+")\n"
                cont+=1
                #print(produto.get_id(),"- "+produto.get_titulo(),sep="") #Implementar (Livro, mídia digital)
            escolhido = entrada_saida.exibir_lista_geral_produtos(opcao_invalida,lista,cont)

            if escolhido > self.coleta_ultimo_id():
                opcao_invalida = True
            else:
                return escolhido
        
    # def coleta_ultimo_id(self):
    #     cont = 1
    #     for produto in self.__lista_produto:
    #         cont+=1
    #     return cont
        
    def buscar_produto(self, id):
        for produto in self.__lista_produto:
            if(produto.get_id() == id):
                validacao.validar_exibicao_busca(produto)
                return produto
        return None
    
    def alugar_produto(self, produto, lista_usuarios,estoque):
        cliente = lista_usuarios.buscar_cliente(entrada_saida.solicitar_rg_aluguel())
        if (cliente):
            tempo_aluguel = validacao.confirmar_tempo_aluguel()
            validacao.confirmar_aluguel(cliente, produto, tempo_aluguel,estoque)
        else: #Fazer as tratativas
            print("Cliente não encontrado")
            print(cliente)