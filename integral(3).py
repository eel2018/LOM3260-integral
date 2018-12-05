import scipy.integrate as sp
from numpy import *

def integral(f, a, b):
    
    '''
        f é uma string com uma fórmula em x
            por exemplo, f = 'sin(x)+x**2'
            
        a e b são floats
    '''
    # define uma função func à partir de f
    #   usando o comando eval
    def func(x):
        return eval(f)
    # calcula a integral usando scipy.integrate.quad
    valor, erro = sp.quad(func, a, b)
    
    return valor
