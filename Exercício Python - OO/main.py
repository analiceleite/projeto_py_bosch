from EntradaSaida import EntradaSaida
import Processamento


def Main():
    match MenuInicial():
        case 1:
            MenuCadastro()

def MenuInicial():
    return EntradaSaida.menuOpcoes()

def MenuCadastro():
    match EntradaSaida.menuCadastro():
        case 1:
            Processamento.cadastrarLivro()
            
Main()