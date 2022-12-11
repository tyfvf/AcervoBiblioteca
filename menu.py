from datetime import datetime
from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo

def cadastrar_usuarios(usuarios):
    nome = input('Qual o nome do usuário? ')
    usuarios.append(Usuario(len(usuarios), nome))
    print('Usuário cadastrado!')


def listar_usuarios(usuarios):
    if len(usuarios) == 0:
        print('Nenhum usuário cadastrado ainda')
    else:
        for u in usuarios:
            print(u)


def cadastrar_livros(livros):
    nome = input('Qual o nome do livro? ')
    livros.append(Livro(len(livros), nome))
    print('Livro cadastrado com sucesso!')


def listar_livros(livros):
    if len(livros) == 0:
        print('Nenhum livro cadastrado ainda')
    else:
        for l in livros:
            print(l)


def pegar_livro(usuarios, livros, emprestimos):
    id = int(input('Qual o id do usuário que irá pegar? '))
    if id < 0 or id >= len(usuarios):
        print('Esse ID não existe')
    else:
        id_livro = int(input(f'Bem-vindo {usuarios[id].nome}, qual o id do livro que você quer pegar? '))
        if id_livro < 0 or id_livro >= len(livros):
            print('Esse ID não existe')
        elif livros[id_livro].emprestado:
            print('Esse livro foi emprestado, por favor aguarde.')
        else:
            emprestimos.append(Emprestimo(len(emprestimos), usuarios[id], livros[id_livro], datetime.now()))
            livros[id_livro].emprestado = True
            print(f'{usuarios[id].nome} pegou {livros[id_livro].nome} emprestado!')


def registro_emprestimos(emprestimos):
    if len(emprestimos) == 0:
        print('Nenhum empréstimo feito')
    else:
        for e in emprestimos:
            print(e)


def devolver_livro(emprestimos):
    id_emprestimo = int(input('Qual o id do empréstimo? '))
    if id_emprestimo < 0 or id_emprestimo >= len(emprestimos):
        print('Esse ID não existe')
    elif emprestimos[id_emprestimo].devolvido:
        print('Esse empréstimo já está quitado')
    else:
        emprestimos[id_emprestimo].livro.emprestado = False
        emprestimos[id_emprestimo].devolvido = True
        emprestimos[id_emprestimo].data_entrega = datetime.now()
        print('Livro devolvido com sucesso!')
        