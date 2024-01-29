#EM PYTHON
class Carro(): #classe'carro'
    def __init__(self):
        #atributos da classe
        self.marca = none # atributo
        self.modelo = none # atributo
        self.placa = none # atributo
        self.qdt_de_combustivel = 0

#CRIAR E MODIFICAR
my_car = Carro() #cria objeto

my_car.marca = 'fiat'
my_car.modelo = 'uno'
my_car.placa = 'akdqiwdqw'

#print(my_car.marca)
#print(my_car.modelo)
#print(my_car.placa)

#MÉTODO - abastecer

class Carro(): #define a classe
    def __init__(self):
        #atributos da classe
        self.marca = null # atributo
        self.modelo = null # atributo
        self.placa = null # atributo
        self.qdt_de_combustivel = 0

    def abastecer(self, quantidade):
        self.qdt_de_combustivel += quantidade

#CRIAR E MODIFICAR
my_car = Carro() #cria objeto

my_car.marca = 'fiat'
my_car.modelo = 'uno'
my_car.placa = 'akdqiwdqw'
my_car.abastecer(10)
my_car.abastecer(4)

print(my_car.marca)
print(my_car.modelo)
print(my_car.placa)
print(my_car.qdt_de_combustivel)