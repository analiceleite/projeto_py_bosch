from item_biblioteca import *
from livro import *
from revista import *
from midia_digital import *
from gestao_clientes import *
from datetime import date, timedelta

class estoque_produto:
    def __init__(self):
        self.__lista_produto = []
        self.__lista_produto_alugado = []
        self.__lista_livro = []
        self.__lista_midia_digital = []
        self.__lista_revista = []

    def get_lista_midia_digital(self):
        return self.__lista_midia_digital
    def set_lista_midia_digital(self, value):
        self.__lista_midia_digital = value
    def get_lista_revista(self):
        return self.__lista_revista
    def set_lista_revista(self, value):
        self.__lista_revista = value
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
        #print(produto.get_dono().get_nome())# Método para acessar o nome do dono
        
    def add_lista_livro(self, livro):
        self.__lista_livro.append(livro)

    def add_lista_midia_digital(self, midia_digital):
        self.__lista_midia_digital.append(midia_digital)

    def add_lista_revista(self, revista):
        self.__lista_revista.append(revista)

    def opcao_menu_busca(quant_estoque):
        return entrada_saida.menu_buscar(quant_estoque,False)
    
    def exibir_lista_geral(estoque,lista_usuarios):
        operacao_nao_cancelada = True
        opcao_invalida = False
        while operacao_nao_cancelada:
            produto_em_busca = estoque.exibir_lista_produto()
            produto_localizado = estoque.buscar_produto(produto_em_busca)
            if (produto_localizado):
                entrada = entrada_saida.solicitar_menu_sim_nao_editar(artes_ascii.menu_busca_encontrado, opcao_invalida, 25)
                if entrada in (1,2,3):
                    match entrada:
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
                disponibilidade = self.verifica_disponibilidade(produto.get_tipo())
                lista += "["+str(produto.get_id()) + "]- " + str(produto.get_titulo()) + " ("+str(produto.get_tipo())+") - "+disponibilidade+"\n"
                cont+=1
            escolhido = entrada_saida.exibir_lista_geral_produtos(opcao_invalida,lista)
            if escolhido > self.coleta_ultimo_id():
                opcao_invalida = True
            else:
                return escolhido
    
    def verifica_disponibilidade(self,tipo):
        if tipo == "Livro":
            lista = self.__lista_livro
        elif tipo == "Revista":
            lista = self.__lista_revista
        else:
            lista = self.__lista_midia_digital

        for produto in lista:
            if produto.get_locatario() == None:
                return "Em estoque"
        return "Fora de estoque"
    
    def coleta_ultimo_id(self):
        cont = 1
        for produto in self.__lista_produto:
            cont+=1
        return cont
        
    def buscar_produto(self, id):
        nao_encontrado = False
        for produto in self.__lista_produto:
            if(produto.get_id() == id):
                validacao.validar_exibicao_busca(produto)
                if produto.get_tipo() == "Livro":
                    lista = self.__lista_livro
                elif produto.get_tipo() == "Mídia Digital":
                    lista = self.__lista_midia_digital
                else:
                    lista = self.__lista_revista
                for iter in lista:
                    if (iter.get_locatario() == None):
                        return iter
                nao_encontrado = True
        if (nao_encontrado):
            return None
        else:
            return False
    
    def alugar_produto(self, produto, lista_usuarios,estoque):
        cliente = lista_usuarios.buscar_cliente(entrada_saida.solicitar_rg_aluguel())
        if (cliente):
            tempo_aluguel = validacao.confirmar_tempo_aluguel(False, cliente)
            data_atual = date.today()
            data_prov = date.today() + timedelta(days=tempo_aluguel)
            data_retirada = data_atual.strftime("%d/%m/%Y")
            data_devolutiva = data_prov.strftime("%d/%m/%Y")
            if(validacao.confirmar_aluguel(cliente, produto, data_retirada, data_devolutiva,estoque)):
                entrada_saida.exibir_confirmacao_aluguel(cliente, produto)

        else: #Fazer as tratativas
            print("Cliente não encontrado")
            print(cliente)