import sqlite3
import datetime
from tkinter import messagebox
from tkinter import *

class Database():

    def connect(self):
        self.conn = sqlite3.connect('biblioteca.db')
        self.cursor = self.conn.cursor()


    def disconnect(self):
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
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER PRIMARY KEY, 
                usuario_id INTEGER NOT NULL,
                livro_id INTEGER NOT NULL,
                data_saida DATE NOT NULL,
                data_entrega DATE DEFAULT NULL,
                devolvido BOOLEAN NOT NULL DEFAULT False,
                FOREIGN KEY (usuario_id) references usuarios (id),
                FOREIGN KEY (livro_id) references livros (id)
                );
        """)
        self.conn.commit()

        self.disconnect()

    
    def novo_usuario(self):
        self.nome = self.entry_nome_usuario.get()

        if self.nome == '':
            messagebox.showwarning('Perigo!', 'Você não pode adicionar um usuario no banco de dados sem um nome!')
            self.entry_nome_usuario.focus()
        else:
            self.connect()
            self.cursor.execute("""INSERT INTO usuarios (nome) VALUES (?)""", (self.nome,))
            self.conn.commit()
            self.disconnect()
            self.cadastrar_usuario_top_level.destroy()


    def novo_livro(self):
        self.nome = self.entry_nome_livro.get()

        if self.nome == '':
            messagebox.showwarning('Perigo!', 'Você não pode adicionar um livro no banco de dados sem um nome!')
            self.entry_nome_livro.focus()
        else:
            self.connect()
            self.cursor.execute("""INSERT INTO livros (nome) VALUES (?)""", (self.nome,))
            self.conn.commit()
            self.disconnect()
            self.cadastrar_livro_top_level.destroy()


    def novo_emprestimo(self):
        self.id_usuario = self.entry_id_usuario.get()
        self.id_livro = self.entry_id_livro.get()

        try:
            self.connect()
            data = self.cursor.execute("""SELECT emprestado FROM livros WHERE id = ?""", (self.id_livro,))
            emprestado = next(data)[0]
            data = self.cursor.execute("""SELECT id FROM usuarios WHERE id = ?""", (self.id_usuario,))
            next(data)
            self.disconnect()
        except StopIteration:
            messagebox.showwarning('Erro!', 'Você não pode fazer um empréstimo sem adicionar um id válido para usuário e livro (se necessário, consulte a lista de usuários e livros para saber o id)!')
            self.entry_id_livro.focus()
            return
        
        if emprestado:
            messagebox.showwarning('Livro já emprestado!', 'O livro que você quer pegar já está sendo emprestado no momento!')
            self.entry_id_livro.focus()
        else:
            self.connect()
            self.cursor.execute("""INSERT INTO emprestimos (usuario_id, livro_id, data_saida) VALUES (?, ?, ?)""", (self.id_usuario, self.id_livro, datetime.date.today()))
            self.cursor.execute("""UPDATE livros SET emprestado = ? WHERE id = ?""", (True, self.id_livro))
            self.conn.commit()
            self.disconnect()
            self.pegar_livro_top_level.destroy()


    def devolucao(self):
        self.id_usuario = self.entry_id_usuario_devolver.get()
        self.id_livro = self.entry_id_livro_devolver.get()

        try:
            self.connect()
            existe = self.cursor.execute("""SELECT id FROM emprestimos WHERE usuario_id = ? AND livro_id = ? AND devolvido = ?""", (self.id_usuario, self.id_livro, False))
            existe = next(existe)[0]
            self.disconnect()
        except StopIteration:
            messagebox.showwarning('Erro!', 'Você não pode devolver um livro sem adicionar um id válido para usuário e livro (se necessário, consulte a lista de usuários e livros para saber o id)!')
            self.entry_id_livro_devolver.focus()
            return
        
        self.connect()
        self.cursor.execute("""UPDATE livros SET emprestado = ? WHERE id = ?""", (False, self.id_livro))
        self.cursor.execute("""UPDATE emprestimos SET devolvido = ?, data_entrega = ? WHERE id = ?""", (True, datetime.date.today(), existe))
        self.conn.commit()
        self.disconnect()
        self.devolver_livro_top_level.destroy()


    def mostrar_usuarios(self):
        self.tree_usuarios.delete(*self.tree_usuarios.get_children())
        self.connect()
        data = self.cursor.execute("""SELECT id, nome FROM usuarios ORDER BY nome ASC;""")
        for i in data:
            self.tree_usuarios.insert('', END, values=i)
        self.disconnect()


    def mostrar_livros(self):
        self.tree_livros.delete(*self.tree_livros.get_children())
        self.connect()
        data = self.cursor.execute("""SELECT id, nome, emprestado FROM livros ORDER BY nome ASC;""")
        data_formatada = []
        for i in data:
            data_formatada = list(i)
            if data_formatada[2] == 0:
                data_formatada[2] = 'Não'
            else:
                data_formatada[2] = 'Sim'
            self.tree_livros.insert('', END, values=data_formatada)
        self.disconnect()


    def mostrar_emprestimos(self):
        self.tree_registro.delete(*self.tree_registro.get_children())
        self.connect()
        data = self.cursor.execute("""SELECT id, usuario_id, livro_id, STRFTIME("%d/%m/%Y", data_saida), data_entrega, devolvido FROM emprestimos ORDER BY id ASC;""")
        data_formatada = []
        for i in data:
            data_formatada = list(i)
            self.connect()
            data_formatada[1] = next(self.cursor.execute("""SELECT nome FROM usuarios WHERE id = ?""", (data_formatada[1],)))[0]
            data_formatada[2] = next(self.cursor.execute("""SELECT nome FROM livros WHERE id = ?""", (data_formatada[2],)))[0]
            self.disconnect()
            if data_formatada[4] != None:
                format = data_formatada[4].split('-')
                data_formatada[4] = f"{format[2]}/{format[1]}/{format[0]}"
                atrasado = datetime.datetime.strptime(data_formatada[4], "%d/%m/%Y") - datetime.datetime.strptime(data_formatada[3], "%d/%m/%Y")
                if atrasado.days >= 7:
                    data_formatada[5] = 'Sim - COM ATRASO'
            if data_formatada[5] == 0:
                data_formatada[5] = 'Não'
            elif data_formatada[5] == 1:
                data_formatada[5] = 'Sim'
            self.tree_registro.insert('', END, values=data_formatada)
        self.disconnect()
        