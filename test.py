import unittest
from biseccion import *
from newton import *
from polinomio_taylor import *
from integral_rienmann import *
from trapecio import *

class test(unittest.TestCase):
    def testBiseccion(self):
        print('\n\nMetodo de biseccion\n')
        f1 = lambda x: math.exp(x) - 3 * x ** 2
        f2 = lambda x: math.sin(x) - math.exp(x)**-x
        self.assertEqual(biseccion(f1, 1, 2, 0.5, 10),None)
        self.assertEqual(biseccion(f2, 0.50, 1, 0.04, 5),0.6875)
    
    def testNewton(self):
        print('\n\nMetodo de Newton-Rapson\n')
        f1 = lambda x: math.sin(x) - math.exp(-x)
        f2 = lambda x: math.exp(x) - 3 * x**2
        self.assertEqual(newton(f1,1,2,10),[1])
        self.assertEqual(newton(f2,1,4,10),[1])
    
    def testTaylor(self):
        print('\n\nPolinomio de Taylor\n')
        f1 = lambda x: (x + 2)**2
        f2 = lambda x: x**2 + math.cos(x)
        self.assertEqual(pol_taylor(f1,1),6.030000000000039)
        self.assertEqual(pol_taylor(f2,2),3.1270806960477535)
    
    def testRiemann(self):
        print('\n\nIntegral de Riemann\n')
        f1 = lambda x: x/(x**2+1)
        f2 = lambda x: x*math.cos(x**2)
        self.assertEqual(integral_riemann(f1, 0, 1, 4),0)
        self.assertEqual(integral_riemann(f2, 1, 2, 6),0)   
    
    def testTrapecio(self):
        print('\n\nMetodo del Trapecio\n')
        f1 = lambda x: math.cos(x-1)
        f2 = lambda x: x*math.cos(1-x**2)
        self.assertEqual(trapecio(f1, 1, 2, 4),2.0618406287594926)
        self.assertEqual(trapecio(f2, 2, 3, 4),-67.43866203908323)
            
        
if __name__ == '__main__':
    unittest.main()   