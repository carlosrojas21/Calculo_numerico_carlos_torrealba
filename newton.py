import math
def der(f, h = 0.02):
    def d(x): #esta funcion es para sacar la derivada de la funcion a utilizar
        return (f(x + h) - f(x))/h
    return der

def newton(f, x0, Er, N):
    Ei = 1; result = list()
    i = 0; result.append(x0)
    x1 = 0  
    while (Ei > Er) and (i < N): #aqui el ciclo continuara hasta cumplir las dos condiciones
        print('\nIteracion: ',i+1)
        df = der(f) #se asigna la derivada a una variable para utilizarla
        x0 = x0 - (f(x0)/df(x0)) #se usa la formula sacar x0  
        result.append(x1)
        Ei = math.fabs((x1-x0)/x1)#aqui se comprueba si el error es menor al indicado
        print('Valor del Error: ',Ei)
        i = i+1 #de no ser asi se realiza otra iteracion con x0 siendo asignado a x1
        x0 = x1
    return result    