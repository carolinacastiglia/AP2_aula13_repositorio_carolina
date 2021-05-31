from Pilha import Pilha

p = Pilha()

p.imprimir() #pilha apenas inicializada
p.remover()  #pilha apenas inicializada

p.adicionar(10)
p.adicionar(15)
p.adicionar(18)
p.adicionar(6)

p.imprimir()

p.remover() #remover topo 6
p.imprimir()
p.remover() #remover topo 18
p.imprimir()
p.remover() #remover topo 15
p.imprimir()

p.adicionar(98)
p.imprimir()
p.adicionar(2)
p.imprimir()

p.remover() #remover topo 2
p.imprimir()
p.remover() #remover topo 98
p.imprimir()
p.remover() #remover topo 10
p.imprimir()
p.remover() #tentativa de remover após remover todos elementos

p.adicionar(35)
p.adicionar(73)
p.imprimir()