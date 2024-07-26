import math

def integral_riemann(f, a, b, n):
    area = 0
    h = (b-a)/n #Calculo del valor de h o el intervalo entre los dos puntos
    print('valor de H: ',h)
    for i in range(n):
        area + f(a+i*h)*h #calculo del area total
        print('Area: ',area)      
    return area