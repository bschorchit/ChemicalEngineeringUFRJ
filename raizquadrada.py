import metodos
from math import sqrt

def F(x):
    F = 18 - x**2
    return F

metodos.bissecao(F)
metodos.regulafalsa(F)
metodos.newtonraphson(F)
metodos.secante(F)

