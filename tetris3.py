from tkinter import *

# Dimensões do jogo
quadradoLado = 20
qtdQuadradosLargura = 10
qtdQuadradosAltura = 20
# Define a altura e a largura da tela
largura = quadradoLado * qtdQuadradosLargura
altura = quadradoLado * qtdQuadradosAltura


# A classe Peca é responsável por criar e renderizar a peça no Tetris
class Peca:

    def __init__(self, linha, coluna, tipo):
        self.linha = linha
        self.coluna = coluna
        # self.grade[][]
        # self.tamanho
        if(tipo == 1):
            self.grade = [[0, 0, 0], [1, 1, 0], [0, 1, 1]]
            self.tamanho = 3

    # Método responsável por girar uma peça no jogo
    def vira(self, Tela):
        # Cria um array de cópia para armazenar a peça a ser giradea
        copia = [[0 for indiceLinha in range(
            self.tamanho)] for indiceColuna in range(self.tamanho)]

        # Faz a cópia girar a peça
        for lin in range(self.tamanho):
            for col in range(self.tamanho):
                copia[self.tamanho - 1 - col][lin] = self.grade[lin][col]

        # Verifica colisão do array de cópia com algo da tela
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if copia[indiceLinha][indiceColuna] * (self.coluna+indiceLinha) >= qtdQuadradosAltura:
                    return 0
                if copia[indiceLinha][indiceColuna] == 1 and Tela.grade[self.coluna+indiceLinha][self.linha+indiceColuna] != 0:
                    return 0
        # Copia os valores do array cópia para a grade
        for lin in range(self.tamanho):
            for col in range(self.tamanho):
                self.grade[lin][col] = copia[lin][col]
        return 1

    def desce(self, Tela):
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if self.grade[indiceLinha][indiceColuna] * (self.coluna+1+indiceLinha) >= qtdQuadradosAltura:
                    return 0
                if self.grade[indiceLinha][indiceColuna] == 1 and Tela.grade[self.coluna+indiceLinha+1][self.linha+indiceColuna] * self.grade[indiceLinha][indiceColuna] != 0:
                    return 0
        self.coluna = self.coluna + 1
        return 1

    # Método que permite a movimentação à direita na grade da tela
    def direita(self, Tela):
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if self.grade[indiceLinha][indiceColuna] * (self.linha+1+indiceLinha) >= qtdQuadradosLargura:
                    return 0
                if Tela.grade[self.coluna][self.linha+1] * self.grade[indiceLinha][indiceColuna] != 0:
                    return 0
        self.linha = self.linha + 1
        return 1

    # Método que permite a movimentação à esquerda na grade da tela
    def esquerda(self, Tela):
        for indiceLinha in range(self.tamanho):
            for indiceColuna in range(self.tamanho):
                if self.grade[indiceLinha][indiceColuna] * (self.linha-1+indiceLinha) < 0:
                    return 0
                if Tela.grade[self.coluna][self.linha+1] * self.grade[indiceLinha][indiceColuna] != 0:
                    return 0
        self.linha = self.linha - 1
        return 1

# A classe tela é responsável por criar a grade da tela, que será renederizada pelo canvas na classe Tetris


class Tela:

    def __init__(self):
        # Define uma matriz e itera por ela usando [[], []]
        self.grade = [[0 for indiceLinha in range(qtdQuadradosLargura)]
                      for indiceColuna in range(qtdQuadradosAltura)]

    # Método responsável por adicionar peças ao jogo conforme forem caindo as anteriores
    def addPecas(self, peca):
        for lin in range(peca.tamanho):
            for col in range(peca.tamanho):
                if peca.grade[lin][col] != 0:
                    self.grade[lin+peca.coluna][col +
                                                peca.linha] = peca.grade[lin][col]

# A classe Tetris é a classe inicializadora do jogo, nesta classe define-se o canvas para renderizar
# a grade da tela e define o método run().


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
        self.window.bind("<Up>", self.gira)

    def gira(self, event):
        self.peca.vira(self.tela)

    def moverParaEsquerda(self, event):
        self.peca.esquerda(self.tela)

    def moverParaDireita(self, event):
        self.peca.direita(self.tela)

    def desenha(self):
        for indiceLinha in range(self.peca.tamanho):
            for indiceColuna in range(self.peca.tamanho):
                if self.peca.grade[indiceLinha][indiceColuna] != 0:
                    self.canvas.create_polygon(
                        [(self.peca.linha + indiceColuna) * quadradoLado,
                         (self.peca.coluna + indiceLinha) * quadradoLado,
                         (self.peca.linha + indiceColuna) *
                         quadradoLado + quadradoLado,
                         (self.peca.coluna + indiceLinha) * quadradoLado,
                         (self.peca.linha + indiceColuna) *
                         quadradoLado + quadradoLado,
                         (self.peca.coluna + indiceLinha) *
                         quadradoLado + quadradoLado,
                         (self.peca.linha + indiceColuna) * quadradoLado,
                         (self.peca.coluna + indiceLinha)*quadradoLado+quadradoLado], fill='green')

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
        tempoDescida = 0
        while(True):
            # O delete('All') está especificando que a cada vez que a peça descer pela grade, a
            # renderização do bloco anterior, e o anterior a este, serão deletados, ficando apenas a principal.
            self.canvas.delete('all')

            if tempoDescida == 5:
                desceu = self.peca.desce(self.tela)
                tempoDescida = 0
                if desceu == 0:
                    self.tela.addPecas(self.peca)
                    self.peca = Peca(3, 1, 1)

            else:
                tempoDescida += 1

            self.desenha()

            self.canvas.after(50)
            self.window.update_idletasks()
            self.window.update()


game = Tetris()
game.run()
