from relatorio import Relatorio
from livro import Livro
from usuario import Usuario

def menu():
    # Dados simulados
    Livro.livros_cadastrados.append(Livro("1984", "George Orwell", "Ficção", 2, 1949))
    Livro.livros_cadastrados.append(Livro("Dom Casmurro", "Machado de Assis", "Romance", 3, 1899))
    Livro.livros_cadastrados.append(Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 1, 1937))

    while True:
        print("\n=== MENU DA BIBLIOTECA ===")
        print("1. Consultar livros")
        print("2. Fazer empréstimo")
        print("3. Devolver livro")
        print("4. Cadastrar usuário")
        print("5. Cadastrar Livro")
        print("6. Relatórios")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                usuario_temp = Usuario("Consulta", "temp", "temp@email.com")
                usuario_temp.consultar_livros()
            case "2":
                usuario_temp = Usuario("Emprestimo", "temp", "temp@email.com")
                usuario_temp.emprestimo_livros()
            case "3":
                usuario_temp = Usuario("Devolucao", "temp", "temp@email.com")
                usuario_temp.devolucao_livros()
            case "4":
                Usuario.cadastrar_usuario()
            case "5":
                Usuario.cadastrar_livro()
            case "6":
                submenu_relatorios()
            case "7":
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

def submenu_relatorios():
    while True:
        print("\n--- RELATÓRIOS ---")
        print("1. Livros disponíveis")
        print("2. Livros emprestados")
        print("3. Usuários cadastrados")
        print("4. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                Relatorio.listar_livros_disponiveis()
            case "2":
                Relatorio.listar_livros_emprestados()
            case "3":
                Relatorio.listar_usuarios()
            case "4":
                break
            case _:
                print("Opção inválida.")

menu()