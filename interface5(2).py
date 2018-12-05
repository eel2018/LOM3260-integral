# importando bibliotecas
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import tkinter.filedialog as fld
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# importando arquivo que possui a função que realiza a integração
import integral as integ

# definindo classe que será usada pra tudo
class Everything:
    
    def __init__(self,master):
        self.janela(master)
    
    # definindo função janela
    def janela(self,master):
        #definindo menu superior
        menu = tk.Menu()
        #definindo um submenu
        submenu = tk.Menu(menu)
        root.config(menu = menu)
        # *********  BARRA DE MENU  ********
        # definindo nomes dos menus e os comandos à eles associados
        menu.add_command(label='Salvar...',command= self.salvar_arquivo)
        menu.add_cascade(label='Help',menu= submenu)
        submenu.add_command(label='Manual...',command= self.abre_manual)
        submenu.add_command(label='Tutorial...',command= self.tutorial)
        menu.add_command(label='Sobre...',command= self.mostrar_info)
        
        #*******  FRAME  *********    
        # definindo frames
        self.frame= None    
        frameGrafico= ttk.Frame()
        frameEntrada= ttk.Frame()
        #definindo localização dos frames
        frameGrafico.pack(side='left')
        frameEntrada.pack(side='right')
        
        #*******    ROTULOS  ***** 
        # definindo textos que aparecerão na janela
        care=ttk.Label(frameEntrada,text='Funciona somente com a incógnita x!')   
        f=ttk.Label(frameEntrada,text='f(x):')
        intA=ttk.Label(frameEntrada,text='A:')
        intB=ttk.Label(frameEntrada,text='B:')
        resp=tk.Label(frameEntrada,text="Valor da integral =")
        title=ttk.Label(frameEntrada,text='Título:')
        eixox=ttk.Label(frameEntrada,text='Eixo x:')
        eixoy=ttk.Label(frameEntrada,text='Eixo y:')
        
        # definindo onde esses textos aparecerão, row = linha, column = coluna)
        f.grid(row=1,column=1,sticky='W',padx=10,pady=10)
        intA.grid(row=2,column=1,sticky='W',padx=10,pady=10)
        intB.grid(row=2,column=2,sticky='W',padx=10,pady=10)
        resp.grid(row=3,column=2,sticky='W',padx=10,pady=10)
        care.grid(row=1,column=2,sticky='W',padx=10,pady=10)
        title.grid(row=4,column=1,sticky='W',padx=10,pady=10)
        eixox.grid(row=5,column=1,sticky='W',padx=10,pady=10)
        eixoy.grid(row=6,column=1,sticky='W',padx=10,pady=10)
        
        # valor da integral
        self.valor_integ=tk.Label(frameEntrada,text='')
        # definindo onde o valor da integral irá aparecer
        self.valor_integ.grid(row=3,column=2,sticky='W',padx=120,pady=10)
        
        #*******    CAMPO DE ENTRADA  *****
        # definindo variáveis
        self.F = tk.StringVar()
        self.A = tk.StringVar()
        self.B = tk.StringVar()
        self.título = tk.StringVar()
        self.eixox = tk.StringVar()
        self.eixoy = tk.StringVar()
        self.valor = tk.StringVar() 
        self.Cria_Grafico(frameGrafico)
        
        #definindo barra onde serão obtidas algumas das variáveis acima
        eF=ttk.Entry(frameEntrada,textvariable=self.F)
        eA=ttk.Entry(frameEntrada,textvariable=self.A)
        eB=ttk.Entry(frameEntrada,textvariable=self.B)
        eX=tk.Entry(frameEntrada,textvariable=self.eixox)
        eY=tk.Entry(frameEntrada,textvariable=self.eixoy)
        eTitle=tk.Entry(frameEntrada,textvariable=self.título)
        
        #definindo localização das barras acima
        eF.grid(row=1,column=1,sticky='W',padx=60,pady=10)
        eA.grid(row=2,column=1,sticky='W',padx=60,pady=10)
        eB.grid(row=2,column=2,sticky='W',padx=30,pady=10)
        eTitle.grid(row=4,column=1,sticky='W',padx=60,pady=10)
        eX.grid(row=5,column=1,sticky='W',padx=60,pady=10)
        eY.grid(row=6,column=1,sticky='W',padx=60,pady=10)
        
        #******  BOTAO  *********
        # definindo botões
        BI=ttk.Button(frameEntrada,text='Integrar',command= self.Mostra_valor)
        BQ=ttk.Button(frameEntrada,text='Sair',command= self.Destroy)
        
        #definindo posicionamento dos botões acima
        BI.grid(row=3,column=1,padx=10,pady=10)
        BQ.grid(row=7,columnspan=7,padx=10,pady=10)
        
        #******  KEYBINDING  *********
        # definindo keybindings, onde pressionar a tecla 'enter' integra a função
        eF.bind("<Return>", lambda event: self.Mostra_valor())
        eA.bind("<Return>", lambda event: self.Mostra_valor())
        eB.bind("<Return>", lambda event: self.Mostra_valor())
        eX.bind("<Return>", lambda event: self.Mostra_valor())
        eY.bind("<Return>", lambda event: self.Mostra_valor())
    
    # definindo função que salva imagem do gráfico
    def salvar_arquivo(self):
        formatos = ( ("formato png","*.png"), ('formato pdf', '*.pdf'), ("formato jpg","*.jpg") )
        filename = fld.asksaveasfilename(initialdir = "./",title = "Exportando a figura...",filetypes = formatos)
        if filename is not '' and filename is not ():
            plt.savefig(filename)
    
    # definindo função de mostrar mensagem de informação
    def mostrar_info(self):
        about_text = '''
        
              Python Integrator
        
              LOM3260 - Computação Científica em Python
        
              Engenharia Física
        
              EEL-USP 2018
             '''
        # título "Info", mensagem referenciada como about_text
        msg.showinfo('Info', about_text)
    
    # definindo função que abre o manual
    def abre_manual(self):
        pass
    
    # definindo função que abre o tutorial
    def tutorial(self):
        pass
    
    # definindo função quer cria gráfico usando matplotlib
    def Cria_Grafico(self, frameGrafico):
        
        # associando self.fig com a função de figura da biblioteca plt
        self.fig = plt.figure()
        # associando self.ax com eixos do gráfico
        self.ax = plt.axes()
        # definindo cor do eixo x
        plt.axhline(0, color='k')
        # definindo cor do eixo y
        plt.axvline(0, color='k')
        
        # definindo área da imagem do gráfico
        canvas = FigureCanvasTkAgg(self.fig, master=frameGrafico)
        canvas.get_tk_widget().pack()
        
    # não permite ao usuário modificar o tamanho horizontal ou vertical da janela
        root.resizable(False, False)
    
    # definindo a função que atualiza o gráfico com os valores fornecidos
    def Atualiza_grafico(self,f,a,b):
        
        # definindo limites da imagem do gráfico a partir dos limites de integração
        x0 = a - abs(a/2)
        x1 = b + abs(b/2)
        #definindo o número de pontos
        N = 100
        # definindo eixos x e y
        x = linspace(a,b,N)
        # eval tenta associar string à uma função
        y = eval(f)
        # apaga a imagem gráfico
        self.ax.cla()
        # plota valores de x e y
        plt.plot(x,y)
        # definindo os limites da imagem do gráfico
        plt.xlim(x0,x1)
    # definindo texto do título, eixo x e eixo y de acordo com variáveis associadas à texto colocado por usuário
        plt.title(self.título.get())
        plt.xlabel(self.eixox.get())
        plt.ylabel(self.eixoy.get())
        # definindo limites de y para imagem do gráfico
        plt.ylim(y.min()-abs((y.min()/5)),y.max()+abs((y.max()/5)))
        # colore região da integral
        plt.fill_between(x,y, color='red', alpha = 0.4)
        self.fig.canvas.draw_idle()

        '''
        define função que mostra o valor da integral de acordo com 
        a função e limites de integração definidas pelo usuário
        '''
    def Mostra_valor(self):
        # valores do limite de integração, necessário que sejam float
        a = float(self.A.get())      
        b = float(self.B.get())
        # função definida pelo usuário, salva na variável self.F
        f = self.F.get()
        # utiliza o aquivo 'integral' para executar a integração
        self.valor = integ.integral(f,a,b)
        # executa função Atualiza_grafico com os valores de f, a,b definidos
        self.Atualiza_grafico(f,a,b)
        # atualiza texto do valor da integral
        self.valor_integ['text'] = str(self.valor)
    
    # define função que fecha a janela
    def Destroy(self):
        # mensagem de sim/não quando a função é executada
        y = msg.askyesno('Sair', 'Deseja realmente sair? Você pode perder informações!')
        # se o usuário escolher "sim" a janela é fechada
        if y is True:
            root.destroy()

# definindo root
root = tk.Tk()
# título da janela
root.title('Python Integrator')
# associando a classe ao root
b = Everything(root)
# mainloop associado à root
root.mainloop()