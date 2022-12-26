from customtkinter import *
from tkinter import ttk
from db import Database

class Menu(Database):

    def cadastrar_usuario(self):
        self.cadastrar_usuario_top_level = CTkToplevel(self.root)
        self.cadastrar_usuario_top_level.title('Cadastrar usuário')
        self.cadastrar_usuario_top_level.resizable(False, False)
        self.cadastrar_usuario_top_level.focus_force()

        self.lb_nome_usuario = CTkLabel(self.cadastrar_usuario_top_level, text='Nome', font=('Arial', 16))
        self.lb_nome_usuario.place(relx=0.15, rely=0.1)

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
        self.tree_usuarios.column('#1', width=5)
        self.tree_usuarios.column('#2', width=100)

        self.tree_usuarios.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.scroll_usuarios = CTkScrollbar(self.listar_usuarios_top_level, orientation=VERTICAL, command=self.tree_usuarios.yview)
        self.tree_usuarios.config(yscrollcommand=self.scroll_usuarios.set)
        self.scroll_usuarios.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.96)

        self.mostrar_usuarios()


    def cadastrar_livro(self):
        self.cadastrar_livro_top_level = CTkToplevel(self.root)
        self.cadastrar_livro_top_level.title('Cadastrar livro')
        self.cadastrar_livro_top_level.resizable(False, False)
        self.cadastrar_livro_top_level.focus_force()

        self.lb_nome_livro = CTkLabel(self.cadastrar_livro_top_level, text='Nome', font=('Arial', 16))
        self.lb_nome_livro.place(relx=0.15, rely=0.1)

        self.entry_nome_livro = CTkEntry(self.cadastrar_livro_top_level, font=('Arial', 12))
        self.entry_nome_livro.place(relx=0.15, rely=0.25)

        self.bt_cadastrar_livro = CTkButton(self.cadastrar_livro_top_level, text='Cadastrar', font=('Arial', 12), command=self.novo_livro)
        self.bt_cadastrar_livro.place(relx=0.15, rely=0.45)


    def listar_livros(self):
        self.listar_livros_top_level = CTkToplevel(self.root)
        self.listar_livros_top_level.title('Listar livros')
        self.listar_livros_top_level.geometry('400x500')
        self.listar_livros_top_level.resizable(False, False)
        self.listar_livros_top_level.focus_force()

        self.tree_livros = ttk.Treeview(self.listar_livros_top_level, height=3, columns=('col1', 'col2', 'col3'))
        self.tree_livros.heading('#0', text='')
        self.tree_livros.heading('#1', text='Id')
        self.tree_livros.heading('#2', text='Nome')
        self.tree_livros.heading('#3', text='Emprestado?')

        self.tree_livros.column('#0', width=1, stretch=NO)
        self.tree_livros.column('#1', width=5)
        self.tree_livros.column('#2', width=100)
        self.tree_livros.column('#3', width=5)

        self.tree_livros.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.scroll_livros = CTkScrollbar(self.listar_livros_top_level, orientation=VERTICAL, command=self.tree_livros.yview)
        self.tree_livros.config(yscrollcommand=self.scroll_livros.set)
        self.scroll_livros.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.96)

        self.mostrar_livros()


    def pegar_livro(self):
        self.pegar_livro_top_level = CTkToplevel(self.root)
        self.pegar_livro_top_level.title('Pegar livro')
        self.pegar_livro_top_level.resizable(False, False)
        self.pegar_livro_top_level.focus_force()

        self.lb_id_livro = CTkLabel(self.pegar_livro_top_level, text='Id do livro', font=('Arial', 16))
        self.lb_id_livro.place(relx=0.15, rely=0.1)

        self.entry_id_livro = CTkEntry(self.pegar_livro_top_level, font=('Arial', 12))
        self.entry_id_livro.place(relx=0.15, rely=0.25)

        self.lb_id_usuario = CTkLabel(self.pegar_livro_top_level, text='Id do usuario', font=('Arial', 16))
        self.lb_id_usuario.place(relx=0.15, rely=0.5)

        self.entry_id_usuario = CTkEntry(self.pegar_livro_top_level, font=('Arial', 12))
        self.entry_id_usuario.place(relx=0.15, rely=0.65)

        self.bt_pegar_livro = CTkButton(self.pegar_livro_top_level, text='Pegar', font=('Arial', 12), command=self.novo_emprestimo)
        self.bt_pegar_livro.place(relx=0.15, rely=0.85)


    def registro_emprestimos(self):
        self.registro_emprestimos_top_level = CTkToplevel(self.root)
        self.registro_emprestimos_top_level.title('Registro de empréstimos')
        self.registro_emprestimos_top_level.geometry('700x500')
        self.registro_emprestimos_top_level.resizable(False, False)
        self.registro_emprestimos_top_level.focus_force()

        self.tree_registro = ttk.Treeview(self.registro_emprestimos_top_level, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.tree_registro.heading('#0', text='')
        self.tree_registro.heading('#1', text='Id')
        self.tree_registro.heading('#2', text='Usuario')
        self.tree_registro.heading('#3', text='Livro')
        self.tree_registro.heading('#4', text='Data de saida')
        self.tree_registro.heading('#5', text='Data de entrega')
        self.tree_registro.heading('#6', text='Devolvido?')

        self.tree_registro.column('#0', width=1, stretch=NO)
        self.tree_registro.column('#1', width=5)
        self.tree_registro.column('#2', width=5)
        self.tree_registro.column('#3', width=5)
        self.tree_registro.column('#4', width=20)
        self.tree_registro.column('#5', width=20)
        self.tree_registro.column('#6', width=5)

        self.tree_registro.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.scroll_registro = CTkScrollbar(self.registro_emprestimos_top_level, orientation=VERTICAL, command=self.tree_registro.yview)
        self.tree_registro.config(yscrollcommand=self.scroll_registro.set)
        self.scroll_registro.place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.96)

        self.mostrar_emprestimos()


    def devolver_livro(self):
        self.devolver_livro_top_level = CTkToplevel(self.root)
        self.devolver_livro_top_level.title('Devolver livro')
        self.devolver_livro_top_level.resizable(False, False)
        self.devolver_livro_top_level.focus_force()

        self.lb_id_livro_devolver = CTkLabel(self.devolver_livro_top_level, text='Id do livro', font=('Arial', 16))
        self.lb_id_livro_devolver.place(relx=0.15, rely=0.1)

        self.entry_id_livro_devolver = CTkEntry(self.devolver_livro_top_level, font=('Arial', 12))
        self.entry_id_livro_devolver.place(relx=0.15, rely=0.25)

        self.lb_id_usuario_devolver = CTkLabel(self.devolver_livro_top_level, text='Id do usuario', font=('Arial', 16))
        self.lb_id_usuario_devolver.place(relx=0.15, rely=0.5)

        self.entry_id_usuario_devolver = CTkEntry(self.devolver_livro_top_level, font=('Arial', 12))
        self.entry_id_usuario_devolver.place(relx=0.15, rely=0.65)

        self.bt_devolver_livro = CTkButton(self.devolver_livro_top_level, text='Devolver', font=('Arial', 12), command=self.devolucao)
        self.bt_devolver_livro.place(relx=0.15, rely=0.85)
            