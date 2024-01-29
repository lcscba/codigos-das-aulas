class Carro():
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.placa = None
        self.qdt_de_combustivel = 0

    def abastecer(self, quantidade):
        if self.qdt_de_combustivel + quantidade > 30:
            print(30- self.qdt_de_combustivel, 'Quantidade maxima para abastecer')
        else:
            self.qdt_de_combustivel += quantidade
        
    def exibir(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Qdt de Combustivel:', self.qdt_de_combustivel)
        
if __name__ == '__main__':
    my_car = Carro()
    my_car.marca = 'fiat'
    my_car.modelo = 'uno'
    my_car.placa = 'okp-5488'
    my_car.abastecer(20)
    my_car.abastecer(15)
    my_car.exibir()
    
    
