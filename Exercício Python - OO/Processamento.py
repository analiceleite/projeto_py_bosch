from EntradaSaida import EntradaSaida
from ItemBiblioteca import ItemBiblioteca


def cadastrarLivro():
    livroEmCadastro = ItemBiblioteca.Livro
    livroEmCadastro.set_titulo(EntradaSaida.solicitarCadastroLivro("o título"))