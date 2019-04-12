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
            self.grade = [[0, 0, 0], [1, 1, 0], [0, 1, 1]]
            self.tamanho = 3

#    def vira(self):

# y é uma linha
# x é coluna
    def desce(self, Tela):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.grade[i][j] * (self.y+1+i) >= qtdQuadradosAltura:
                    return 0
                if self.grade[i][j]==1 and Tela.grade[self.y+i+1][self.x+j] * self.grade[i][j] != 0:
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

    def addPecas(self, peca):
        for lin in range(peca.tamanho):
            for col in range(peca.tamanho):
                if peca.grade[lin][col] != 0:
                    self.grade[lin+peca.y][col+peca.x] = peca.grade[lin][col]


class Tetris:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura,
                             height=altura, bg='black')
        self.canvas.pack()
        self.peca = Peca(3, 1, 1)
        self.numPeca = 0
        self.tela = Tela()

        self.window.bind("<Right>", self.moverParaDireita)
        self.window.bind("<Left>", self.moverParaEsquerda)


   # def gira(self, event):

    def moverParaEsquerda(self, event):
        self.peca.esquerda(self.tela)

    def moverParaDireita(self, event):
        self.peca.direita(self.tela)

    def desenha(self):
        for i in range(self.peca.tamanho):
            for j in range(self.peca.tamanho):
                if self.peca.grade[i][j] != 0:
                    self.canvas.create_polygon(
                        [(self.peca.x + j)* quadradoLado,
                         (self.peca.y + i) * quadradoLado,
                         (self.peca.x + j) * quadradoLado + quadradoLado,
                          (self.peca.y + i) * quadradoLado,
                         (self.peca.x + j) * quadradoLado + quadradoLado,
                          (self.peca.y + i) * quadradoLado + quadradoLado,
                         (self.peca.x + j) * quadradoLado,
                          (self.peca.y + i)*quadradoLado+quadradoLado], fill='green')


        for lin in range(qtdQuadradosAltura):
            for col in range(qtdQuadradosLargura):
                if self.tela.grade[lin][col] != 0:
                    self.canvas.create_polygon(
                        [col*quadradoLado,
                        lin * quadradoLado,
                        col*quadradoLado+quadradoLado,
                        lin*quadradoLado,
                        col*quadradoLado+quadradoLado,
                        lin*quadradoLado+quadradoLado,
                        col*quadradoLado,
                        lin*quadradoLado+quadradoLado], fill="red")

    def run(self):
        time = 0
        while(True):
            self.canvas.delete('all')

            if time == 5: 
                desceu = self.peca.desce(self.tela)
                time = 0
                if desceu == 0:
                    self.tela.addPecas(self.peca)
                    self.peca = Peca (3 , 1, 1)

            else:
                time += 1

            self.desenha()
            
            self.canvas.after(50)
            self.window.update_idletasks()
            self.window.update()


game = Tetris()
game.run()
