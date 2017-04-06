# Name: Paul Prew
# Student Number: 10354828
# Programming for Big Data
# CA 1


# The following are functions that are called by the program named
# 'app_calculator.py'.  


import math
            
def calc_add(num1,num2) :
    result = num1 + num2
    return result

def calc_subtract(num1, num2) :    
    result = num1 - num2
    return result
    
def calc_multiply(num1, num2) :    
    result = num1 * num2
    return result
    
def calc_divide(num1, num2) :
    if num2 == 0:
        result = 'Divide by Zero Error!'
    else:
        result = num1 / num2
    return result
    
def calc_exp(num1, num2) :
    result = num1 ** num2
    return result
    
def calc_squareroot(num) :
    if num  < 0 :
        result = 'Number Error!'
    else :
        result = math.sqrt(num)
    return result
    
def calc_square(num) :
    result = calc_exp(num, 2)
    return result
    
def calc_cube(num) :
    result = calc_exp(num, 3)
    return result

# if degrees = 180 or 360 then sine(degrees) is 0   
def calc_sine(deg):
    if deg % 180 == 0 : result = 0
    else : result = math.sin(math.radians(deg))
    return result

# if degrees = 90 or 270 then cosine(degrees) is 0    
def calc_cosine(deg):
    if (deg - 90)% 180 == 0 : result = 0 
    else : result = math.cos(math.radians(deg))    
    return result
   
 



