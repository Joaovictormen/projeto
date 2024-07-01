class Carrinho:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([ p.valor for p in self.produtos])
    
    def mostrar_produtos(self):
        for produt in self._produtos:
            print(produt.nome, produt.valor)
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
            

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = Carrinho()
p1 = Produto('chocolate', 2)
p2 = Produto('arroz', 10)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.mostrar_produtos()



        