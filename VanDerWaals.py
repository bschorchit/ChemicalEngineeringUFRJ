import metodos

def F(x):
    P = 100
    
    T = 500
    a = 3.59
    b = 0.0427
    R = 0.0821
    F = (R*T)/(x-b) - a/(x**2) - P
    return F

metodos.bissecao(F)
metodos.regulafalsa(F)
metodos.newtonraphson(F)
metodos.secante(F)
