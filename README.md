
# Sistema de Gerenciamento de Biblioteca

Este projeto tem como objetivo criar um sistema de gerenciamento de biblioteca utilizando a linguagem Python, com princípios de Programação Orientada a Objetos (POO) aprendidos no curso de Ciência de Dados (Anhanguera). O sistema permite o cadastro de livros e usuários, além de gerenciar empréstimos e devoluções de livros. Também oferece a funcionalidade de gerar relatórios sobre os livros disponíveis, livros emprestados e usuários cadastrados

## Funcionalidades

- **Cadastro de Livros**: Permite o cadastro de livros na biblioteca com informações como título, autor, gênero, quantidade disponível e ano de publicação.
- **Cadastro de Usuários**: Permite o cadastro de usuários com informações como nome, ID e contato (e-mail).
- **Empréstimo de Livros**: Usuários podem solicitar empréstimos de livros disponíveis, e o sistema atualiza a quantidade de cópias disponíveis.
- **Devolução de Livros**: Usuários podem devolver livros emprestados, e o sistema atualiza a quantidade de cópias disponíveis.
- **Consulta de Livros**: Permite a busca de livros por título, autor ou ano de publicação.
- **Relatórios**: Gera relatórios com a lista de livros disponíveis, livros emprestados e usuários cadastrados.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Princípios**: Programação Orientada a Objetos (POO)
- **Bibliotecas**: Nenhuma biblioteca externa foi utilizada (apenas recursos nativos de Python)

## Como Usar

1. **Clonando o Repositório**:

   Primeiro, clone este repositório para o seu ambiente local:
   
   ```bash
   git clone https://github.com/leticiasss/biblioteca.git
   cd biblioteca
   ```

2. **Estrutura do Código**:

   O projeto é composto pelos seguintes arquivos:
   
   - `livro.py`: Contém a classe `Livro`, que gerencia o cadastro e o controle dos livros na biblioteca.
   - `usuario.py`: Contém a classe `Usuario`, que gerencia o cadastro e os empréstimos de livros pelos usuários.
   - `relatorio.py`: Contém a classe `Relatorio`, responsável pela geração de relatórios sobre os livros e usuários.
   - `main.py` ou `menu.py`: Arquivo principal que executa o menu de opções do sistema.

3. **Executando o Sistema**:

   Após clonar o repositório, basta rodar o arquivo principal (`main.py` ou `menu.py`) para iniciar o sistema. No terminal, execute o seguinte comando:

   ```bash
   python menu.py
   ```

   Isso iniciará o menu interativo do sistema de gerenciamento de biblioteca, onde você poderá:
   - Consultar livros.
   - Fazer empréstimos.
   - Devolver livros.
   - Cadastrar novos usuários.
   - Gerar relatórios.

## Exemplo de Uso

### 1. Cadastro de Livro:
   - Ao iniciar o programa, livros são automaticamente cadastrados, mas você pode adicionar mais livros durante a execução, interagindo com o menu.

### 2. Cadastro de Usuário:
   - O sistema permite que novos usuários se cadastrem, preenchendo nome, ID e e-mail.

### 3. Empréstimo de Livro:
   - Um usuário pode solicitar o empréstimo de um livro, e o sistema verificará se há cópias disponíveis.

### 4. Devolução de Livro:
   - O usuário pode devolver um livro, e o sistema atualizará a quantidade de cópias disponíveis.

### 5. Relatórios:
   - O sistema permite gerar relatórios com as seguintes opções:
     - Livros disponíveis
     - Livros emprestados
     - Usuários cadastrados

## Estrutura do Projeto

```plaintext
biblioteca/
│
├── livro.py          # Classe para gerenciar livros
├── usuario.py        # Classe para gerenciar usuários
├── relatorio.py      # Classe para gerar relatórios
├── menu.py           # Menu principal do sistema
├── README.md         # Este arquivo
```

## Como Contribuir

1. Fork este repositório.
2. Crie uma branch para suas alterações (`git checkout -b minha-branch`).
3. Faça as alterações necessárias e envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
