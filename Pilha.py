from No import No

class Pilha:

    def __init__(self):
       self.topo = None
       self.tamanho = 0
    
    def adicionar(self, valor):
        no = No(valor)

        if self.topo == None:
            self.topo = no
        else:
            aux = self.topo
            self.topo = no
            no.anterior = aux
        self.tamanho += 1

    def imprimir(self):
        txt = ""
        if self.topo == None:
            txt = "A Fila está vazia!"
        else:
            aux = self.topo
            while(aux):
                txt += str(aux.dado)
                aux = aux.anterior
                if aux:
                    txt += " - "
        print(txt,"\n")

    def remover(self):
        if self.topo == None:
            print("Não é possível remover, pois a Fila está vazia!\n")
        else:
            aux = self.topo
            self.topo = aux.anterior

            if self.tamanho != 0:
                if self.tamanho == 1:
                    self.topo == None
                self.tamanho -= 1
            