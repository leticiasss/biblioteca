class Livro:
    livros_cadastrados = []  # Lista de todos os livros cadastrados

    def __init__(self, titulo, autor, genero, ano_publicacao, qntd_disponivel):
        """
        Inicializa um objeto do tipo Livro.

        :param titulo: Título do livro
        :param autor: Autor do livro
        :param genero: Gênero do livro
        :param ano_publicacao: Ano de publicação
        :param qntd_disponivel: Quantidade de exemplares disponíveis
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacao = ano_publicacao
        self.qntd_disponivel = qntd_disponivel
        self.qntd_total = qntd_disponivel

    def cadastrar_livro(self):
        """
        Adiciona o livro atual à lista de livros cadastrados.
        """
        Livro.livros_cadastrados.append(self)
        print(f"O livro '{self.titulo}' foi adicionado com sucesso!")

    @classmethod
    def buscar_por_titulo(cls, titulo):
        """
        Busca livros pelo título (case-insensitive).
        """
        encontrados = []
        for livro in cls.livros_cadastrados:
            if livro.titulo.lower() == titulo.lower():
                encontrados.append(livro)
        return encontrados

    @classmethod
    def buscar_por_autor(cls, autor):
        """
        Busca livros por autor (case-insensitive).
        """
        encontrados = []
        for livro in cls.livros_cadastrados:
            if livro.autor.lower() == autor.lower():
                encontrados.append(livro)
        return encontrados

    @classmethod
    def buscar_por_ano(cls, ano):
        """
        Busca livros por ano de publicação.
        """
        encontrados = []
        for livro in cls.livros_cadastrados:
            if str(livro.ano_publicacao) == str(ano):
                encontrados.append(livro)
        return encontrados
