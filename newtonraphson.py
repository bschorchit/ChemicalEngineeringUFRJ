# MÉTODO NEWTON-RAPHSON - SCRIPT PYTHON
#Estime o volume molar do CO2 a 500K e 100atm
#admitindo que o gás se comporte como um gás de Van der Waals
#equação de Van der Waals: P = (R*T)/(V-b) - a/(V^2)
#equação do erro aproximado: E(%) = abs((xrnovo - xrvelho)/xrnovo)*100

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
#http://docs.sympy.org/latest/tutorial/calculus.html

def F(x):
    P = 100
    T = 500
    a = 3.59
    b = 0.0427
    R = 0.0821
    F = (R*T)/(x-b) - a/(x**2) - P
    return F

def D(xi):
    D = diff(F(x),x)
    Dnum = limit(D,x,xi)
    return Dnum

xi = float(input('Digite um valor para xi'))

xii = xi #valor pra não causar erro no segundo loop

while abs(F(xii)) > 0.0001:
    xiiv = xii
    xii = xi - F(xi)/D(xi)
    xi = xiiv
    print(F(xii))
E = abs(((xii - xi)/xii)*100)
    
if abs(F(xii)) < 0.0001:
    print('Convergiu para xii = ' + str(xii))
    print(E)


#esse script só converge quando xi inicial < 1. Era para acontecer isso mesmo?

