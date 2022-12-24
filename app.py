from customtkinter import *
from tkinter import *
from tkinter import ttk
from menu import Menu

class App(Menu):
    def __init__(self):
        set_default_color_theme('dark-blue')
        set_appearance_mode('dark')
        self.root = CTk()
        self.tela()
        self.tables()
        self.menu()
        self.root.mainloop()
        

    def tela(self):
        self.root.geometry('1000x700+450+150')
        self.root.title('Acervo Biblioteca')
        self.root.resizable(False, False)


    def menu(self):
        self.lb_menu = CTkLabel(self.root, text='Bem-vindo ao acervo da Biblioteca', font=('Times new Roman', 36, 'bold'))
        self.lb_menu.place(relx=0.25, rely=0.05)

        self.bt_cadastro_usuario = CTkButton(self.root, text='Cadastrar usuário', font=('Arial', 14), width=250, command=self.cadastrar_usuario)
        self.bt_cadastro_usuario.place(relx=0.39, rely=0.2)

        self.bt_listar_usuario = CTkButton(self.root, text='Listar usuários', font=('Arial', 14), width=250, command=self.listar_usuarios)
        self.bt_listar_usuario.place(relx=0.39, rely=0.3)

        self.bt_cadastro_livro = CTkButton(self.root, text='Cadastrar livro', font=('Arial', 14), width=250, command=self.cadastrar_livro)
        self.bt_cadastro_livro.place(relx=0.39, rely=0.4)

        self.bt_listar_livro = CTkButton(self.root, text='Listar livros', font=('Arial', 14), width=250, command=self.listar_livros)
        self.bt_listar_livro.place(relx=0.39, rely=0.5)

        self.bt_pegar_livro = CTkButton(self.root, text='Pegar livro', font=('Arial', 14), width=250, command=self.pegar_livro)
        self.bt_pegar_livro.place(relx=0.39, rely=0.6)

        self.bt_registro_emprestimo = CTkButton(self.root, text='Registro de empréstimos', font=('Arial', 14), width=250, command=self.registro_emprestimos)
        self.bt_registro_emprestimo.place(relx=0.39, rely=0.7)

        self.bt_devolver_livro = CTkButton(self.root, text='Devolver livro', font=('Arial', 14), width=250)
        self.bt_devolver_livro.place(relx=0.39, rely=0.8)


App()