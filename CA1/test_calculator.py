# Name: Paul Prew
# Student Number: 10354828
# Programming for Big Data
# CA 1


# The following are a suite of unit tests that are designed to test 
# each of the functions created in the program file named 'functions_calculator.py'. 
# Unit tests are created to test performance for a range of numeric input values,
# including positive/negative numbers and whole/fractional numbers. Tests are also 
# included for exception results and value errors.
# Note: Tests are not included for input values that are non-numeric, as the 
# input validation logic in the app program ensures that only numreric values are entered.


import unittest

from functions_calculator import *

class CalculatorTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(calc_add(2,2), 4)
        self.assertEqual(calc_add(8,3), 11)
        self.assertEqual(calc_add(-6,20), 14)
        self.assertEqual(calc_add(-8,-12), -20)
        self.assertEqual(calc_add(4,-9), -5)
        self.assertEqual(calc_add(8.68, 7.256), 15.936)
        
    def testSubtract(self):  
        self.assertEqual(calc_subtract(8,3), 5)
        self.assertEqual(calc_subtract(3,5), -2)
        self.assertEqual(calc_subtract(4,-9), 13)
        self.assertEqual(calc_subtract(-6,20), -26)
        self.assertEqual(calc_subtract(-8,-12), 4)
        self.assertAlmostEqual(calc_subtract(8.68, 7.256), 1.424)
                    
    def testMultiply(self):  
        self.assertEqual(calc_multiply(5,3), 15)
        self.assertEqual(calc_multiply(4,-2), -8)
        self.assertEqual(calc_multiply(-4,6), -24)  
        self.assertEqual(calc_multiply(-7,-8), 56) 
        self.assertEqual(calc_multiply(6,0), 0) 
        self.assertEqual(calc_multiply(0,6), 0)      
        
    def testDivide(self):
        self.assertEqual(calc_divide(8,2), 4)
        self.assertEqual(calc_divide(10,-2), -5)
        self.assertEqual(calc_divide(-32,4), -8)
        self.assertEqual(calc_divide(-10,-2), 5)        
        self.assertEqual(calc_divide(25.0, 2),12.5) 
        self.assertAlmostEqual(calc_divide(12.45,3.87), 3.21705426) 
        self.assertEqual(calc_divide(4,0), 'Divide by Zero Error!') 
       
    def testExp(self):
        self.assertEqual(calc_exp(5,2), 25)
        self.assertEqual(calc_exp(5,3), 125)
        self.assertEqual(calc_exp(2,4), 16) 
        self.assertEqual(calc_exp(-2,4), 16)
        self.assertEqual(calc_exp(3,0), 1)
        self.assertEqual(calc_exp(5,-3),.008 )
        self.assertAlmostEqual(calc_exp(5,3.66),361.60149376)
        self.assertAlmostEqual(calc_exp(4.876,3),115.92873337)
         
    def testSquareroot(self):
        self.assertEqual(calc_squareroot(25), 5)
        self.assertEqual(calc_squareroot(-5), 'Number Error!') 
        self.assertEqual(calc_squareroot(36), 6)
        self.assertEqual(calc_squareroot(144), 12)
        self.assertEqual(calc_squareroot(0), 0)
        self.assertAlmostEqual(calc_squareroot(150.5), 12.26784414639)
        
    def testSquare(self):
        self.assertEqual(calc_square(5), 25)
        self.assertEqual(calc_square(-5), 25)
        self.assertEqual(calc_square(0), 0)
        self.assertAlmostEqual(calc_square(12.26), 150.3076)
        
    def testCube(self):
        self.assertEqual(calc_cube(5), 125)
        self.assertEqual(calc_cube(-5), -125)
        self.assertEqual(calc_cube(0), 0)
        self.assertAlmostEqual(calc_cube(2.34), 12.812904)
  
    def testSine(self):
        self.assertEqual(calc_sine(0), 0.0)
        self.assertAlmostEqual(calc_sine(30), 0.5)
        self.assertAlmostEqual(calc_sine(60), 0.86602540)
        self.assertAlmostEqual(calc_sine(90), 1.0)
        self.assertAlmostEqual(calc_sine(125), 0.81915204)
        self.assertEqual(calc_sine(180), 0.00)
        self.assertAlmostEqual(calc_sine(270), -1.0)
        self.assertEqual(calc_sine(360), 0.0)
        self.assertAlmostEqual(calc_sine(390), 0.5)      
        self.assertEqual(calc_sine(540), 0.0)
        self.assertAlmostEqual(calc_sine(-30), -0.5)
        self.assertEqual(calc_sine(-180), 0.0)
        self.assertAlmostEqual(calc_sine(305.75), -0.81157398)    
        
    def testCosine(self):
        self.assertAlmostEqual(calc_cosine(0), 1)
        self.assertAlmostEqual(calc_cosine(30), 0.86602540)
        self.assertAlmostEqual(calc_cosine(60), 0.5)
        self.assertEqual(calc_cosine(90), 0.0)
        self.assertAlmostEqual(calc_cosine(125), -0.57357643)
        self.assertAlmostEqual(calc_cosine(180), -1.0)
        self.assertEqual(calc_cosine(270), 0.0)
        self.assertAlmostEqual(calc_cosine(360), 1.0)
        self.assertAlmostEqual(calc_cosine(390), 0.86602540)
        self.assertAlmostEqual(calc_cosine(540), -1.0)
        self.assertAlmostEqual(calc_cosine(-30), 0.86602540)
        self.assertAlmostEqual(calc_cosine(-180), -1.0)
        self.assertAlmostEqual(calc_cosine(305.75), 0.58424966)    
        
     
if __name__ == '__main__':
    unittest.main()


    
    