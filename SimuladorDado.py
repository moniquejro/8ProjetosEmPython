# Simulador de dado
# Simular o uso de um dado, gerando um valor aleatório entre os numeros 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]

    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        try:
            self.eventos == 'sim'
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n' or self.eventos == 'nao':
                print('Agradecemos a sua participacao!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()