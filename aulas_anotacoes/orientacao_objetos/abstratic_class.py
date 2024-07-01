from abc import ABC, abstractmethod

class DarPlay(ABC):
    def __init__(self,tipo_A,nome):
        self.tipo_A = tipo_A
        self.nome = nome
    
    
    def dar_play(self):
        print(f'{self.tipo_A} iniciou...')
    
class Play5(DarPlay):
    ...
        


play5 = Play5('Console','Play5')

print(play5.nome)
print(play5.tipo_A)
play5.dar_play()
        
        