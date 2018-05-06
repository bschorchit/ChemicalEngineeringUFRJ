import metodos
from math import sqrt

def F(x):
    F = sqrt(18) - x
    return F

metodos.bissecao(F)
metodos.regulafalsa(F)
metodos.newtonraphson(F)
metodos.secante(F)

