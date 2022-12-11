class Emprestimo():

    def __init__(self, id, usuario, livro, data_saida):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_saida = data_saida
        self.devolvido = False
        self.data_entrega = None


    def __str__(self):
        if self.devolvido:
            tempo = self.data_entrega - self.data_saida
            if tempo.days > 7:
                return f'{self.id} | {self.usuario.nome} pegou {self.livro.nome} emprestado na data {self.data_saida.strftime("%d/%m/%Y")} - DEVOLVIDO COM ATRASO ({self.data_entrega.strftime("%d/%m/%Y")})'
            else:
                return f'{self.id} | {self.usuario.nome} pegou {self.livro.nome} emprestado na data {self.data_saida.strftime("%d/%m/%Y")} - DEVOLVIDO ({self.data_entrega.strftime("%d/%m/%Y")})'
        else:
            return f'{self.id} | {self.usuario.nome} pegou {self.livro.nome} emprestado na data {self.data_saida.strftime("%d/%m/%Y")}'