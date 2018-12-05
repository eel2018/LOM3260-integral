import tkinter as tk



class Everything:
    def __init__(self,master):
        self.janela()
   
    def janela(self,):
        menu = tk.Menu()
        root.config(menu=menu)
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
        
    #*******  PARTE PRINCIPAL  *********    
        frame_graf = tk.Frame()
        frame_entrada = tk.Frame()  
        frame_graf.pack(side='left')
        frame_entrada.pack(side='left')
    #*******    ROTULOS  *****  
        f =tk.Label(frame_entrada,text= 'f(x):')
        int1 =tk.Label(frame_entrada,text= 'A:')
        int2 =tk.Label(frame_entrada,text= 'B:')
        f.grid(row= 0,collum= 0)
        int1.grid(row= 1,collum= 0)
        int2.grid(row= 1,collum= 2)
    #*******    CAMPO DE ENTRADA  *****
        
        
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
    
            
root = tk.Tk()
b = Everything(root)
root.mainloop()