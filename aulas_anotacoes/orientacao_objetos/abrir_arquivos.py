class Myopen:
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo
        self._arquivo = None
        
    def __enter__(self):
        self._arquivo = open(self.nome_arquivo, self.modo)
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback):
        print("Exit")
        self._arquivo.close()

abrir = Myopen('aula12.txt', 'w') 

with abrir as alguma_coisa:
    print('Abriu')
    alguma_coisa.write("Consegui")


