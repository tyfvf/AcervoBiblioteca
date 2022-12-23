import sqlite3
from tkinter import messagebox
from tkinter import *

class Database():

    def connect(self):
        self.conn = sqlite3.connect('biblioteca.db')
        self.cursor = self.conn.cursor()


    def desconnect(self):
        self.conn.close()


    def tables(self):
        self.connect()

        # Table de usuarios
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY, 
                nome CHAR(40) NOT NULL
                );
        """)
        # Table de livros
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY, 
                nome CHAR(120) NOT NULL, 
                emprestado BOOLEAN NOT NULL DEFAULT False
                );
        """)
        # Table de emprestimos
        # self.cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS emprestimos (
        #         id INTEGER PRIMARY KEY, 
        #         usuario_id INTEGER FOREIGN KEY REFERENCES usuarios(id),
        #         livro_id INTEGER FOREIGN KEY REFERENCES livros(id),
        #         data_saida DATE NOT NULL,
        #         data_entrega DATE DEFAULT NULL,
        #         devolvido BOOLEAN NOT NULL DEFAULT False
        #         );
        # """)
        self.conn.commit()

        self.desconnect()

    
    def novo_usuario(self):
        self.nome = self.entry_nome_usuario.get()

        if self.nome == '':
            messagebox.showwarning('Perigo!', 'Você não pode adicionar um usuario no banco de dados sem um nome!')
            self.entry_nome_usuario.focus()
        else:
            self.connect()
            self.cursor.execute("""INSERT INTO usuarios (nome) VALUES (?)""", (self.nome,))
            self.conn.commit()
            self.desconnect()
            self.cadastrar_usuario_top_level.destroy()


    def mostrar_lista(self, tree):
        tree.delete(*tree.get_children())
        self.connect()
        data = self.cursor.execute("""SELECT id, nome FROM usuarios ORDER BY nome ASC;""")
        for i in data:
            tree.insert('', END, values=i)
        self.desconnect()