# MÉTODO SECANTE - SCRIPT PYTHON
#Estime o volume molar do CO2 a 500K e 100atm
#admitindo que o gás se comporte como um gás de Van der Waals
#equação de Van der Waals: P = (R*T)/(V-b) - a/(V^2)
#equação do erro aproximado: E(%) = abs((xrnovo - xrvelho)/xrnovo)*100

def F(x):
    P = 100
    T = 500
    a = 3.59
    b = 0.0427
    R = 0.0821
    F = (R*T)/(x-b) - a/(x**2) - P
    return F

xi = float(input('Digite um valor para xi'))
xii = float(input('Digite um valor para xii'))

xiii = xii #valor pra não causar erro no segundo loop

while abs(F(xiii)) > 0.0001:
    xiiiv = xiii
    xiii = xii - F(xii)*((xii - xi)/(F(xii) - F(xi)))
    xi = xii
    xii = xiii
    print(F(xii))
E = abs(((xiii - xiiiv)/xiii)*100)
    
if abs(F(xiii)) < 0.0001:
    print('Convergiu para xii = ' + str(xii))
    print(E)


#esse script só converge quando xi e xii inicial < 1. Era para acontecer isso mesmo?
