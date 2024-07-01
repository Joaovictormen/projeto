class Tocar:
    def __init__(self, nome):
        self.nome = nome
    

    def __call__(self, *args ,**kwds):
        print(f'{self.nome} está tocando...')

guitar = Tocar("guitar")
guitar()