from tkinter import *

# Dimensões do jogo
quadradoLado = 20
qtdQuadradosAltura = 20
qtdQuadradosLargura = 10
largura = quadradoLado * qtdQuadradosLargura
altura = quadradoLado * qtdQuadradosAltura


class Peca:

    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        # self.grade[][]
        # self.tamanho
        if(tipo == 1):
            self.grade = [[0, 1, 0], [0, 1, 1], [0, 0, 1]]
            self.tamanho = 3

#    def vira(self):

# y é uma linha
# x é coluna
    def desce(self, Tela):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if Tela.grade[self.y+1][self.x] * self.grade[i][j] != 0:
                    return 0
        self.y = self.y + 1
        return 1

#    def direita(self):

#    def esquerda(self):


class Tela:

    def __init__(self):
        # Define uma matriz e itera por ela usando [[], []]
        self.grade = [[0 for i in range(qtdQuadradosAltura)]
                      for j in range(qtdQuadradosLargura)]


class Tetris:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura,
                             height=largura, bg='black')
        self.canvas.pack()
        self.peca = Peca(3, 1, 1)
        self.numPeca = 0
        self.tempo = Tela()

   # def gira(self, event):

   # def moverParaEsquerda(self, event):

#    def moverParaDireita(self, event):

    def desenha(self):
        for i in range(self.peca.tamanho):
            for j in range(self.peca.tamanho):
                if self.peca.grade[i][j] != 0:
                    self.canvas.create_polygon(
                        [self.peca.x * quadradoLado,
                         self.peca.y * quadradoLado,
                         self.peca.x * quadradoLado + quadradoLado,
                         self.peca.y * quadradoLado,
                         self.peca.x * quadradoLado + quadradoLado,
                         self.peca.y * quadradoLado + quadradoLado,
                         self.peca.x * quadradoLado,
                         self.peca.y*quadradoLado+quadradoLado], fill='green')

    def run(self):
        while(True):
            self.canvas.delete('all')
            self.desenha()
            self.peca.desce(self.tempo)
            self.canvas.after(1180)
            self.window.update_idletasks()
            self.window.update()


game = Tetris()
game.run()
