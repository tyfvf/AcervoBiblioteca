from customtkinter import *
from tkinter import *
from tkinter import ttk
from datetime import datetime
from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo
from db import Database

class Menu(Database):

    def cadastrar_usuario(self):
        self.cadastrar_usuario_top_level = CTkToplevel(self.root)
        self.cadastrar_usuario_top_level.title('Cadastrar usuário')
        self.cadastrar_usuario_top_level.resizable(False, False)
        self.cadastrar_usuario_top_level.focus_force()

        self.lb_nome_usuario = CTkLabel(self.cadastrar_usuario_top_level, text='Nome', font=('Arial', 16))
        self.lb_nome_usuario.place(relx=0.4, rely=0.1)

        self.entry_nome_usuario = CTkEntry(self.cadastrar_usuario_top_level, font=('Arial', 12))
        self.entry_nome_usuario.place(relx=0.15, rely=0.25)

        self.bt_cadastrar_usuario = CTkButton(self.cadastrar_usuario_top_level, text='Cadastrar', font=('Arial', 12), command=self.novo_usuario)
        self.bt_cadastrar_usuario.place(relx=0.15, rely=0.45)


    def listar_usuarios(self):
        self.listar_usuarios_top_level = CTkToplevel(self.root)
        self.listar_usuarios_top_level.title('Listar usuários')
        self.listar_usuarios_top_level.geometry('400x500')
        self.listar_usuarios_top_level.resizable(False, False)
        self.listar_usuarios_top_level.focus_force()

        self.tree_usuarios = ttk.Treeview(self.listar_usuarios_top_level, height=3, columns=('col1', 'col2'))
        self.tree_usuarios.heading('#0', text='')
        self.tree_usuarios.heading('#1', text='Id')
        self.tree_usuarios.heading('#2', text='Nome')

        self.tree_usuarios.column('#0', width=1, stretch=NO)
        self.tree_usuarios.column('#1', width=100)
        self.tree_usuarios.column('#2', width=400)

        self.tree_usuarios.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.scroll_usuarios = CTkScrollbar(self.listar_usuarios_top_level, orientation=VERTICAL, command=self.tree_usuarios.yview)
        self.tree_usuarios.config(yscrollcommand=self.scroll_usuarios.set)
        self.scroll_usuarios.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.96)

        self.mostrar_lista(self.tree_usuarios)


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
            