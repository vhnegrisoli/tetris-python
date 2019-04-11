from tkinter import *

class Tetris:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura, height=largura, bg='black')
        self.canvas.pack

    def run(self):
        while(True):
            self.canvas.after(50)
            self.window.update_iddletasks()
            self.window.update()
g = Game()
g.run()