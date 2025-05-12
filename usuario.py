from livro import Livro

class Usuario:
    usuarios_cadastrados = []  # Lista de usuários

    def __init__(self, nome, id, contato):
        """
        Inicializa um objeto do tipo Usuario.

        :param nome: Nome do usuário
        :param id: Identificador único do usuário
        :param contato: Contato (e-mail, telefone etc.)
        """
        self.nome = nome
        self.id = id
        self.contato = contato

    @classmethod
    def cadastrar_usuario(cls):
        """
        Método para cadastrar um novo usuário via entrada do console.
        """
        print("\n--- Cadastro de Usuário ---")
        nome = input("Nome: ")
        id = input("ID: ")
        contato = input("Email para contato: ")

        # Verifica se já existe um usuário com o mesmo contato
        for u in cls.usuarios_cadastrados:
            if u.contato == contato:
                print("Este e-mail já está cadastrado.")
                return

        novo_usuario = Usuario(nome, id, contato)
        cls.usuarios_cadastrados.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")

    def buscar_livro_por_nome(self, nome_livro):
        """
        Busca livros pelo nome.
        """
        encontrados = []
        for livro in Livro.livros_cadastrados:
            if livro.titulo.lower() == nome_livro.lower():
                encontrados.append(livro)
        return encontrados

    def emprestimo_livros(self):
        """
        Realiza o empréstimo de um livro se houver cópias disponíveis.
        """
        nome = input("Digite o nome do livro que você quer emprestado: ")
        encontrados = self.buscar_livro_por_nome(nome)

        if encontrados:
            for livro in encontrados:
                print(50 * '-')
                if livro.qntd_disponivel < 1:
                    print("Não tem mais nenhuma cópia disponível para empréstimo!")
                else:
                    livro.qntd_disponivel -= 1
                    print(f"Você está pegando 1 cópia de '{livro.titulo}'.")
                    print(f"Ainda restam {livro.qntd_disponivel} cópias disponíveis.")
        else:
            print("Não encontramos seu livro ):")

    def devolucao_livros(self):
        """
        Devolve um livro e aumenta a quantidade de cópias disponíveis.
        """
        nome = input("Digite o nome do livro que você quer devolver: ")
        encontrados = self.buscar_livro_por_nome(nome)

        if encontrados:
            for livro in encontrados:
                print(50 * '-')
                livro.qntd_disponivel += 1
                print(f"Você devolveu o livro '{livro.titulo}'.")
                print(f"Agora existem {livro.qntd_disponivel} cópias disponíveis.")
        else:
            print("Livro não cadastrado.")

    def consultar_livros(self):
        """
        Permite ao usuário consultar livros por título, autor ou ano de publicação.
        """
        print("\n--- Consulta de Livros ---")
        print("1. Por título")
        print("2. Por autor")
        print("3. Por ano de publicação")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título: ")
            encontrados = Livro.buscar_por_titulo(titulo)
        elif opcao == "2":
            autor = input("Digite o autor: ")
            encontrados = Livro.buscar_por_autor(autor)
        elif opcao == "3":
            ano = input("Digite o ano de publicação: ")
            encontrados = Livro.buscar_por_ano(ano)
        else:
            print("Opção inválida.")
            return

        if encontrados:
            for livro in encontrados:
                print(50 * '-')
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Gênero: {livro.genero}")
                print(f"Ano de publicação: {livro.ano_publicacao}")
                print(f"Disponíveis: {livro.qntd_disponivel}")
        else:
            print("Nenhum livro encontrado com esse critério.")
