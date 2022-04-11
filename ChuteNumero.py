# Projeto 3 - Chute o número
# Objetivo: criar um algoritimo que gera um valor aleátorio e o usuário tenta adivinhar até acertar
import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 100
        self.valor_minimo = 1
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Chute um valor mais baixo!')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValorAleatorio()
            self.tentar_novamente == False
            print('Parabéns!')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)