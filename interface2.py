import tkinter as tk
#import scipy.integrate as sp
from tkinter import ttk


class Everything:
    def __init__(self,master):
        self.janela(master)
   
    def janela(self,master):
        menu = tk.Menu()
        root.config(menu = menu)
    # *********  BARRA DE MENU  ********
        submenu = tk.Menu(menu)
        menu.add_cascade(label="file",menu=submenu)
        submenu.add_command(label='novo...',command= self.reiniciar)
        submenu.add_command(label='salvar...',command= self.salvar_arquivo)
        menu.add_command(label='sobre...',command= self.mostrar_info)
        submenu2 = tk.Menu(menu)
        menu.add_cascade(label='help',menu= submenu2)
        submenu2.add_command(label='manual...',command= self.abre_manual)
        submenu2.add_command(label='tutorial...',command= self.tutorial)
        submenu2.add_command(label='suicidio...',command= self.suicidio)
    #*******  TOOLBAR  ********
    
    #*******  PARTE PRINCIPAL  *********    
        self.frame= None    
        frameGrafico= ttk.Frame()
        frameEntrada= ttk.Frame()
        frameGrafico.pack(side='left')
        frameEntrada.pack(side='right')
    #*******    ROTULOS  ***** 
        care=ttk.Label(frameEntrada,text='Funciona somente com a incognita x!')   
        f=ttk.Label(frameEntrada,text='f(x):')
        intA=ttk.Label(frameEntrada,text='A:')
        intB=ttk.Label(frameEntrada,text='B:')
        f.grid(row=1,column=1,sticky='W',padx=10,pady=10)
        intA.grid(row=2,column=1,sticky='W',padx=10,pady=10)
        intB.grid(row=2,column=3,sticky='W',padx=10,pady=10)
        care.grid(row=1,column=4,sticky='N',padx=10,pady=10)
    #*******    CAMPO DE ENTRADA  *****
        self.F = tk.StringVar()
        self.A = tk.StringVar()
        self.B = tk.StringVar()
        ef=ttk.Entry(frameEntrada,textvariable=self.F)
        eA=ttk.Entry(frameEntrada,textvariable=self.A)
        eB=ttk.Entry(frameEntrada,textvariable=self.B)
        ef.grid(row=1,column=2,sticky='W',padx=10,pady=10)
        eA.grid(row=2,column=2,sticky='W',padx=10,pady=10)
        eB.grid(row=2,column=4,sticky='W',padx=10,pady=10)
    #******  BOTAO  *********
        BI=ttk.Button(frameEntrada,text='Integrate',command= self.ip)
        BQ=ttk.Button(frameEntrada,text='Quit',command= master.destroy)
        BI.grid(row=3,columnspan=7,padx=10,pady=10)
        BQ.grid(row=4,columnspan=7,padx=10,pady=10)
        
        
        
   
    def ip(self):
        pass
    def reiniciar(self):
        pass
    def salvar_arquivo(self):
        pass
    def mostrar_info(self):
        pass
    def abre_manual(self):
        pass
    def tutorial(self):
        pass
    def suicidio(self):
        pass
    '''def funçao(self):
        
        c = int(self.F)
        return c
    def intergral(self,funçao,a,b):
        self.valor,self.erro =sp.quad(funçao,self.a,self.b)'''
        
    
            
root = tk.Tk()
b = Everything(root)
root.mainloop()