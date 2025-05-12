from livro import Livro
from usuario import Usuario

class Relatorio:

    @staticmethod
    def listar_livros_disponiveis():
        """
        Lista todos os livros com ao menos uma cópia disponível.
        """
        print("\n--- Livros Disponíveis ---")
        encontrou = False
        for livro in Livro.livros_cadastrados:
            if livro.qntd_disponivel > 0:
                encontrou = True
                print(50 * '-')
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Gênero: {livro.genero}")
                print(f"Ano: {livro.ano_publicacao}")
                print(f"Disponíveis: {livro.qntd_disponivel}")
        if not encontrou:
            print("Nenhum livro disponível no momento.")

    @staticmethod
    def listar_livros_emprestados():
        """
        Lista os livros que têm pelo menos uma cópia emprestada.
        """
        print("\n--- Livros Emprestados ---")
        encontrou = False
        for livro in Livro.livros_cadastrados:
            emprestados = livro.qntd_total - livro.qntd_disponivel
            if emprestados > 0:
                encontrou = True
                print(50 * '-')
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Gênero: {livro.genero}")
                print(f"Ano: {livro.ano_publicacao}")
                print(f"Emprestados: {emprestados}")
        if not encontrou:
            print("Nenhum livro emprestado no momento.")

    @staticmethod
    def listar_usuarios():
        """
        Lista todos os usuários cadastrados.
        """
        print("\n--- Usuários Cadastrados ---")
        if not Usuario.usuarios_cadastrados:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in Usuario.usuarios_cadastrados:
            print(50 * '-')
            print(f"Nome: {usuario.nome}")
            print(f"ID: {usuario.id}")
            print(f"Contato: {usuario.contato}")
