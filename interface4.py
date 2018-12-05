import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import integral as integ
import tkinter.filedialog as fld
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Everything:
    
    def __init__(self,master):
        self.janela(master)
        
    def janela(self,master):
        menu = tk.Menu()
        root.config(menu = menu)
    # *********  BARRA DE MENU  ********
        submenu = tk.Menu(menu)
        menu.add_cascade(label="File",menu=submenu)
        submenu.add_command(label='novo...',command= self.reiniciar)
        submenu.add_command(label='salvar...',command= self.salvar_arquivo)
        submenu2 = tk.Menu(menu)
        menu.add_cascade(label='Help',menu= submenu2)
        submenu2.add_command(label='Manual...',command= self.abre_manual)
        submenu2.add_command(label='Tutorial...',command= self.tutorial)
        menu.add_command(label='Sobre...',command= self.mostrar_info)
    #*******  TOOLBAR  ********
    
    #*******  PARTE PRINCIPAL  *********    
        self.frame= None    
        frameGrafico= ttk.Frame()
        frameEntrada= ttk.Frame()
        frameGrafico.pack(side='left')
        frameEntrada.pack(side='right')
        
        #*******  PARTE do gráfico  *********    
        self.Cria_Grafico(frameGrafico)
        
    #*******    ROTULOS  ***** 
        care=ttk.Label(frameEntrada,text='Funciona somente com a incógnita x!')   
        f=ttk.Label(frameEntrada,text='f(x):')
        
        self.valor = tk.StringVar()       
        
        intA=ttk.Label(frameEntrada,text='A:')
        intB=ttk.Label(frameEntrada,text='B:')
        resp=tk.Label(frameEntrada,text="Valor da integral =")
        eixox=ttk.Label(frameEntrada,text='Eixo x:')
        eixoy=ttk.Label(frameEntrada,text='Eixo y:')
        f.grid(row=1,column=1,sticky='W',padx=10,pady=10)
        intA.grid(row=2,column=1,sticky='W',padx=10,pady=10)
        intB.grid(row=2,column=3,sticky='W',padx=10,pady=10)
        resp.grid(row=3,column=1,sticky='W',padx=10,pady=10)
        care.grid(row=1,column=4,sticky='N',padx=10,pady=10)
        eixox.grid(row=4,column=1,sticky='W',padx=10,pady=10)
        eixoy.grid(row=5,column=1,sticky='W',padx=10,pady=10)
        
        self.valor_integ=tk.Label(frameEntrada,text='')
        self.valor_integ.grid(row=3,column=2,sticky='W',padx=10,pady=10)
        
    #*******    CAMPO DE ENTRADA  *****
       #self.F = tk.StringVar()
        self.F = tk.StringVar()
        self.A = tk.StringVar()
        self.B = tk.StringVar()
        self.eixox = tk.StringVar()
        self.eixoy = tk.StringVar()
        
        eF=ttk.Entry(frameEntrada,textvariable=self.F)
        eA=ttk.Entry(frameEntrada,textvariable=self.A)
        eB=ttk.Entry(frameEntrada,textvariable=self.B)
        eX=tk.Entry(frameEntrada,textvariable=self.eixox)
        eY=tk.Entry(frameEntrada,textvariable=self.eixoy)
        eF.grid(row=1,column=2,sticky='W',padx=10,pady=10)
        eA.grid(row=2,column=2,sticky='W',padx=10,pady=10)
        eB.grid(row=2,column=4,sticky='W',padx=10,pady=10)
        eX.grid(row=4,column=2,sticky='W',padx=10,pady=10)
        eY.grid(row=5,column=2,sticky='W',padx=10,pady=10)
    #******  BOTAO  *********
        BI=ttk.Button(frameEntrada,text='Integrar',command= self.Mostra_valor)
        BQ=ttk.Button(frameEntrada,text='Sair',command= self.Destroy)
        BI.grid(row=6,columnspan=7,padx=10,pady=10)
        BQ.grid(row=7,columnspan=7,padx=10,pady=10)
        
    
        eF.bind("<Return>", lambda event: self.Mostra_valor())
        eA.bind("<Return>", lambda event: self.Mostra_valor())
        eB.bind("<Return>", lambda event: self.Mostra_valor())
        eX.bind("<Return>", lambda event: self.Mostra_valor())
        eY.bind("<Return>", lambda event: self.Mostra_valor())
    
    def reiniciar(self):
        pass
    def salvar_arquivo(self):
        formatos = ( ("formato png","*.png"), ('formato pdf', '*.pdf'), ("formato jpg","*.jpg") )
        filename = fld.asksaveasfilename(initialdir = "./",title = "Exportando a figura...",filetypes = formatos)
        if filename is not '' and filename is not ():
            plt.savefig(filename)
        
    def mostrar_info(self):
        about_text = '''
        
              Python Integrator
        
              LOM3260 - Computação Científica em Python
        
              Engenharia Física
        
              EEL-USP 2018
             '''
             
        msg.showinfo('Info', about_text)
        
    def abre_manual(self):
        pass
    def tutorial(self):
        pass
    
    def Cria_Grafico(self, frameGrafico):
        
        self.fig = plt.figure()
        self.ax = plt.axes()
        plt.axhline(0, color='k')
        plt.axvline(0, color='k')
        plt.title('Gráfico da Integral')

        # frame
        grafico_frame = tk.Frame(frameGrafico)
        grafico_frame.pack()

        # canvas
        canvas = FigureCanvasTkAgg(self.fig, master=frameGrafico)
        canvas.get_tk_widget().pack()
        
        root.resizable(False, False)         # não permite ao usuário modificar o tamanho horizontal ou vertical da janela
    
    def Atualiza_grafico(self,f,a,b):
        x0 = a - abs(a/2)
        x1 = b + abs(b/2)
        N = 100
        x = linspace(a,b,N)
        y = eval(f)
        self.ax.cla()
        plt.plot(x,y)
        plt.xlim(x0,x1)
        plt.xlabel(self.eixox.get())
        plt.ylabel(self.eixoy.get())
        plt.ylim(y.min()-abs((y.min()/5)),y.max()+abs((y.max()/5)))
        plt.fill_between(x,y, alpha = 0.3)
        self.fig.canvas.draw_idle()
        
    
    def Mostra_valor(self):
        a = float(self.A.get())
        b = float(self.B.get())
        f = self.F.get()
        self.valor = integ.integral(f,a,b)
        self.Atualiza_grafico(f,a,b)
        self.valor_integ['text'] = str(self.valor)
        
    def Destroy(self):
        y = msg.askyesno('Sair', 'Deseja realmente sair? Você pode perder informações!')
        if y is True:
            root.destroy()

root = tk.Tk()
root.title('Python Integrator')
b = Everything(root)
root.mainloop()