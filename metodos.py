#equação do erro aproximado: E(%) = abs((xrnovo - xrvelho)/xrnovo)*100

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
#http://docs.sympy.org/latest/tutorial/calculus.html
# esse import é necessário para o newtonraphson, mas o import não pode
#estar inserido dentro da função, por isso tem que ficar aqui fora


# MÉTODO DA BISSEÇÃO
def bissecao(F):
    def P(x,y):
        Prod = F(x)*F(y)
        return Prod
    
    xi = float(input('Digite um valor para xi'))
    xii = float(input('Digite um valor para xii'))

    xr = 100 #valor qualquer pra não causar erro no primeiro loop
    E = 100 #valor qualquer pra não causar erro no primeiro loop

    while abs(P(xi,xii)) > 0.0000001 or E > 10:
    
        if P(xi,xii)<0:
            xrv = xr
            xr = (xi + xii)/2
            E = abs(((xr - xrv)/xr)*100)
    
            if P(xi,xr)<0:
                xii = xr

            if P(xr,xii)<0:
                xi = xr

            if P(xi,xr)==0:
                xi = xr
                E = 0
                break
    
        else:
            print('Intervalo ruim, Fi = ' + str(F(xi)) + ' e Fii = ' + str(F(xii)))
            break
    
    if abs(P(xi,xii)) < 0.0000001 and E < 10:
        print('Convergiu para xr = ' + str(xr))
        print(P(xi,xii))
        print(E)


# MÉTODO REGULA FALSA
def regulafalsa(F):
    def P(x,y):
        Prod = F(x)*F(y)
        return Prod
    
    xi = float(input('Digite um valor para xi'))
    xii = float(input('Digite um valor para xii'))

    xr = 100 #valor qualquer pra não causar erro no primeiro loop
    E = 100 #valor qualquer pra não causar erro no primeiro loop

    while abs(P(xi,xii)) > 0.0000001 or E > 10:
    
        if P(xi,xii)<0:
            xrv = xr
            xr = xii - F(xii)*((xi - xii)/(F(xi) - F(xii)))
            E = abs(((xr - xrv)/xr)*100)

            if P(xi,xr)<0:
                xii = xr

            if P(xr,xii)<0:
                xi = xr

            if P(xi,xr)==0:
                xi = xr
                E = 0
                break
              
        else:
            print('Intervalo ruim, Fi = ' + str(F(xi)) + ' e Fii = ' + str(F(xii)))
            break
        
    if abs(P(xi,xii)) < 0.0000001 and E < 10:
        print('Convergiu para xr = ' + str(xr))
        print(P(xi,xii))
        print(E)


# MÉTODO NEWTON RAPHSON
def newtonraphson(F):

    def D(xi):
        D = diff(F(x),x)
        Dnum = limit(D,x,xi)
        return Dnum

    xi = float(input('Digite um valor para xi'))

    xii = xi #valor pra não causar erro no segundo loop

    while abs(F(xii)) > 0.0000001:
        xiiv = xii
        xii = xi - F(xi)/D(xi)
        xi = xiiv
        print(F(xii))
    E = abs(((xii - xi)/xii)*100)
    
    if abs(F(xii)) < 0.0000001:
        print('Convergiu para xii = ' + str(xii))
        print(E)


# MÉTODO SECANTE
def secante(F):
    xi = float(input('Digite um valor para xi'))
    xii = float(input('Digite um valor para xii'))

    xiii = xii #valor pra não causar erro no segundo loop

    while abs(F(xiii)) > 0.0000001:
        xiiiv = xiii
        xiii = xii - F(xii)*((xii - xi)/(F(xii) - F(xi)))
        xi = xii
        xii = xiii
        print(xiii)
    E = abs(((xiii - xiiiv)/xiii)*100)
    
    if abs(F(xiii)) < 0.0000001:
        print('Convergiu para xii = ' + str(xii))
        print(E)
