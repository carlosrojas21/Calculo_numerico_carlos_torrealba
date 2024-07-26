import math; #importamos la libreria math en todas las funciones

def biseccion(f, a, b, e, n):
    #'f' es la funcion
    #'a' el punto inicial 
    #'b' el punto final 
    #'e' el error
    #'n' las iteraciones  
    for i in range(n): 
        print('\nIteracion: ', i+1)  
        m = (a + b)/2 #esta es la formula para realizar las iteraciones
        print('\nValor actual: ', m)
        f_m = f(m)
        if abs(f_m) < e:
            return m  #este condicional es para devolver el valor de m en caso que sea menor que el error
        
        if f(a) * f_m < 0: 
            b = m
            print('\nValor actual de B: ',b)
        else:  #aqui se asigna el valor actual de m en a o b dependiendo de si es mayor o menor al anterior punto
            a = m
            print('\nValor actual de A: ',a)
        #en caso que el error no se pueda calcular el resultado devolvera 'None'
    return None          
            
            
