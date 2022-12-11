import menu

escolha = None
usuarios = []
livros = []
emprestimos = []

print('Bem-vindo a biblioteca virtual!')

while escolha != 8:
    print('O que você deseja fazer?')
    print('1 - Cadastrar usuário')
    print('2 - Listar usários')
    print('3 - Cadastrar livro')
    print('4 - Listar livros')
    print('5 - Pegar um livro')
    print('6 - Registro de empréstimos')
    print('7 - Devolver um livro')
    print('8 - Sair')

    escolha = int(input('> '))

    match escolha:
        case 1:
            menu.cadastrar_usuarios(usuarios)
        case 2:
            menu.listar_usuarios(usuarios)
        case 3:
            menu.cadastrar_livros(livros)
        case 4:
            menu.listar_livros(livros)
        case 5:
            menu.pegar_livro(usuarios, livros, emprestimos)
        case 6:
            menu.registro_emprestimos(emprestimos)
        case 7:
            menu.devolver_livro(emprestimos)
        case 8:
            print('Até mais!')
        case _:
            print('Número inválido')