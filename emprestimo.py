class Emprestimo():

    def __init__(self, id, usuario, livro, devolvido=False):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.devolvido = devolvido


    def __str__(self):
        if self.devolvido:
            return f'{self.id} | {self.usuario.nome} pegou {self.livro.nome} emprestado - DEVOLVIDO'
        else:
            return f'{self.id} | {self.usuario.nome} pegou {self.livro.nome} emprestado'