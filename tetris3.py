from tkinter import *

# Dimensões do jogo
quadradoLado = 20
qtdQuadradosLargura = 10
qtdQuadradosAltura = 20
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
                if self.grade[i][j] * (self.y+1+i) >= qtdQuadradosAltura:
                    return 0
                if Tela.grade[self.y+1][self.x] * self.grade[i][j] != 0:
                    return 0
        self.y = self.y + 1
        return 1

    def direita(self, Tela):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.grade[i][j] * (self.x+1+i) >= qtdQuadradosLargura:
                    return 0
                if Tela.grade[self.y][self.x+1] * self.grade[i][j] != 0:
                    return 0
        self.x = self.x + 1
        return 1

    def esquerda(self, Tela):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.grade[i][j] * (self.x-1+i) < 0:
                    return 0
                if Tela.grade[self.y][self.x+1] * self.grade[i][j] != 0:
                    return 0
        self.x = self.x - 1
        return 1


class Tela:

    def __init__(self):
        # Define uma matriz e itera por ela usando [[], []]
        self.grade = [[0 for i in range(qtdQuadradosLargura)]
                      for j in range(qtdQuadradosAltura)]


class Tetris:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura,
                             height=altura, bg='black')
        self.canvas.pack()
        self.peca = Peca(3, 1, 1)
        self.numPeca = 0
        self.tempo = Tela()

        self.window.bind("<Right>", self.moverParaDireita)
        self.window.bind("<Left>", self.moverParaEsquerda)


   # def gira(self, event):

    def moverParaEsquerda(self, event):
        self.peca.esquerda(self.tempo)

    def moverParaDireita(self, event):
        self.peca.direita(self.tempo)

    def desenha(self):
        for i in range(self.peca.tamanho):
            for j in range(self.peca.tamanho):
                if self.peca.grade[j][i] != 0:
                    self.canvas.create_polygon(
                        [(self.peca.x + j)* quadradoLado,
                         (self.peca.y + i) * quadradoLado,
                         (self.peca.x + j) * quadradoLado + quadradoLado,
                          (self.peca.y + i) * quadradoLado,
                         (self.peca.x + j) * quadradoLado + quadradoLado,
                          (self.peca.y + i) * quadradoLado + quadradoLado,
                         (self.peca.x + j) * quadradoLado,
                          (self.peca.y + i)*quadradoLado+quadradoLado], fill='green')

    def run(self):
        time = 0
        while(True):
            self.canvas.delete('all')

            if time == 5: 
                self.peca.desce(self.tempo)
                time = 0
            else:
                time += 1

            self.desenha()
            
            self.canvas.after(50)
            self.window.update_idletasks()
            self.window.update()


game = Tetris()
game.run()
