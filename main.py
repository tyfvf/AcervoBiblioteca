from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo

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
            nome = input('Qual o nome do usuário? ')
            usuarios.append(Usuario(len(usuarios), nome))
            print('Usuário cadastrado!')
        case 2:
            if len(usuarios) == 0:
                print('Nenhum usuário cadastrado ainda')
            else:
                for u in usuarios:
                    print(u)
        case 3:
            nome = input('Qual o nome do livro? ')
            livros.append(Livro(len(livros), nome))
            print('Livro cadastrado com sucesso!')
        case 4:
            if len(livros) == 0:
                print('Nenhum livro cadastrado ainda')
            else:
                for l in livros:
                    print(l)
        case 5:
            id = int(input('Qual o id do usuário que irá pegar? '))
            if len(usuarios) == 0 or id < 0 or id > len(usuarios):
                print('Esse ID não existe')
            else:
                id_livro = int(input(f'Bem-vindo {usuarios[id].nome}, qual o id do livro que você quer pegar? '))
                if len(livros) == 0 or id_livro < 0 or id_livro > len(livros):
                    print('Esse ID não existe')
                elif livros[id_livro].emprestado:
                    print('Esse livro foi emprestado, por favor aguarde.')
                else:
                    emprestimos.append(Emprestimo(len(emprestimos), usuarios[id], livros[id_livro]))
                    livros[id_livro].emprestado = True
                    print(f'{usuarios[id].nome} pegou {livros[id_livro].nome} emprestado!')
        case 6:
            if len(emprestimos) == 0:
                print('Nenhum empréstimo feito')
            else:
                for e in emprestimos:
                    print(e)
        case 7:
            id = int(input('Qual o id do usuário que irá devolver? '))
            if len(usuarios) == 0 or id < 0 or id > len(usuarios):
                print('Esse ID não existe')
            else:
                id_livro = int(input(f'Qual o id do livro que você quer devolver {usuarios[id].nome}? '))
                if len(livros) == 0 or id_livro < 0 or id_livro > len(livros):
                    print('Esse ID não existe')
                elif not livros[id_livro].emprestado:
                    print('Esse livro não está emprestado.')
                else:
                    existe = False
                    for e in emprestimos:
                        if usuarios[id].id == e.usuario.id and livros[id_livro].id == e.livro.id:
                            existe = True
                            e.devolvido = True

                    if existe:
                        livros[id_livro].emprestado = False
                        print('Livro devolvido com sucesso!')
                    else:
                        print('Não foi esse usuário a quem foi emprestado o livro.')
        case 8:
            print('Até mais!')
        case _:
            print('Número inválido')