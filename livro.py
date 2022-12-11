class Livro():

    def __init__(self, id, nome, emprestado=False):
        self.id = id
        self.nome = nome
        self.emprestado = emprestado


    def __str__(self):
        if self.emprestado:
            return f'{self.id} | {self.nome} - EMPRESTADO'
        else:
            return f'{self.id} | {self.nome}'
            