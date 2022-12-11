escolha = None

print('Bem-vindo a biblioteca virtual!')

while escolha != 8:
    print('O que você deseja fazer?')
    print('1 - Cadastrar Aluno')
    print('2 - Listar Alunos')
    print('3 - Cadastrar Livro')
    print('4 - Listar Livro')
    print('5 - Pegar um livro')
    print('6 - Registro de empréstimos')
    print('7 - Devolver um livro')
    print('8 - Sair')

    escolha = int(input('> '))

    match escolha:
        case 1:
            print('1')
        case 2:
            print('1')
        case 3:
            print('1')
        case 4:
            print('1')
        case 5:
            print('1')
        case 6:
            print('1')
        case 7:
            print('1')
        case 8:
            print('Até mais!')
        case _:
            print('Número inválido')