import tkinter as tk
import tkinter.messagebox as msg
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import algoritmos as alg

class interface_grafica:
    def __init__(self):
        self.criajanela()
        
        
    def criajanela(self):
        self.janela = tk.Tk()
        barraMenu = tk.Frame()
        barraMenu.pack()
        Bmenu = tk.Button(barraMenu,text = 'menu')
        Bsobre = tk.Button(barraMenu,text = 'sobre')
        Bsocorro = tk.Button(barraMenu,text = 'help')
        Bmenu.pack()
        Bsobre.pack(side='left')
        Bsocorro.pack(side='left')
janela=self.janela
janela.mainloop()