# MÉTODO DA BISSEÇÃO - SCRIPT PYTHON
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

def P(x,y):
    Prod = F(x)*F(y)
    return Prod

xi = float(input('Digite um valor para xi'))
xii = float(input('Digite um valor para xii'))

xr = 100 #valor qualquer pra não causar erro no primeiro loop
E = 100 #valor qualquer pra não causar erro no primeiro loop

while abs(P(xi,xii)) > 0.0001 or E > 10:
    
    if P(xi,xii)<0:
        xrv = xr
        xr = (xi + xii)/2
        E = abs(((xr - xrv)/xr)*100)

        if P(xi,xr)<0:
            xii = xr

        if P(xr,xii)<0:
            xi = xr

    else:
        print('Intervalo ruim, Fi = ' + str(F(xi)) + ' e Fii = ' + str(F(xii)))
        break
    
if abs(P(xi,xii)) < 0.0001 and E < 10:
    print('Convergiu para xr = ' + str(xr))
    print(P(xi,xii))
    print(E)

