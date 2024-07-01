class Carro:

    def __init__(self) :
        self.pneus = None
    
    def ligar_carro(self):

        if self.pneus == 4:
            print('O carro está em perfeito funcionamento')
        else:
            print('Número de pneus incorreto')
    
    def adicionar_pneus(self, pneus):
        self.pneus = pneus.qtd_pneu
        
class Compra_pneu:
    
    def __init__(self, qtd_pneu):
        self.qtd_pneu = qtd_pneu

carro = Carro()
compra_pneu = Compra_pneu(4)

carro.adicionar_pneus(compra_pneu)
carro.ligar_carro()

        