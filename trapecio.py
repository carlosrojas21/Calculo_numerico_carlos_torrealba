import math

def trapecio(f,a,b,n):
    area = 0
    h=(b-a)/n 
    x0 = a 
    for i in range(n):  
        x1 = x0+(i+1)/h  #aqui se saca el valor de x1 para despues sacar el valor de la funcion en ese punto
        print('\nValor de x1: ',x1)
        area = area+(h/2)+(f(x0)+f(x1)) #aqui se empieza a calcular el area para cada iteracion
        print('\nValor del area: ',area)
        x0 = x1
    return area    