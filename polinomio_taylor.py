import math

def pol_taylor(f,x,h=0.03):
    
    polinomio = (f(x+h)-f(x))/h #en este caso para el polinomio de taylor solo se aplico la formula directamente
    print('Resultado: ',polinomio)#despues solo se devuelve el resultado de la operacion
    return polinomio
                