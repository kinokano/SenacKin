class calebe():
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'

teste = calebe('calebe')
print(teste)