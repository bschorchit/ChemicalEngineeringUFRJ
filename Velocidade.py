import metodos
from math import exp

def F(x):
    g = 9.81
    m = 68.1
    t = 10
    v = 40
    F = ((g*m)/x)*(1-exp(-x*t/m)) - v
    return F

metodos.bissecao(F)
metodos.regulafalsa(F)
metodos.newtonraphson(F)
metodos.secante(F)
