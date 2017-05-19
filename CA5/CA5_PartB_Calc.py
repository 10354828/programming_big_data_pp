# Name: Paul Prew
# Student Number: 10354828
# Programming for Big Data
# CA 5 - Part B

# python functions to perform calculations on lists of numbers

# declaration of variables used in function calls
celsius_temps = [-5.5, 0.0, 15.8, 24.6]
fahrenheit_temps = [22.1, 32.3, 60, 76.3]
num_list = [47, 11, 42, 13]
num_list1 = [47.5, 11.4, 42, 13]
num_list2 = [1000, 2, 5, 4]
num_list3 = [1000,0, 5, 4]
num_list4 = [1000, 'Nan', 5, 4]

# formula to convert from celsius to fahrenheit
def fahrenheit(t):
    return ((float(9)/5)*t + 32)

# formula to convert from fahrenheit to celsius    
def celsius(t):
    return (float(5)/9*(t - 32))

# calc function to get max value - using 'reduce' & 'lambda'
def max(values):
    return reduce(lambda a,b: a if (a>b) else b, values)

# calc function to get min value - using 'reduce' & 'lambda'
def min(values):
    return reduce(lambda a,b: a if (a<b) else b, values)  

# calc function to get addition result - using 'reduce' & 'lambda'    
def add(values):    
    return reduce(lambda a,b: a+b, values) 

# calc function to get subtraction result - using 'reduce' & 'lambda'
def subtract(values):    
    return reduce(lambda a,b: a-b, values)    

# calc function to get multiplication result - using 'reduce' & 'lambda'
def multiply(values):    
    return reduce(lambda a,b: a*b, values)  

# calc function to get division result - using 'reduce' & 'lambda'
def divide(values):    
    return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan', values)      

# calc function to get even numbers - using 'filter' & 'lambda'        
def is_even(values):    
    return filter(lambda x: x % 2 == 0, values)  

# calc function to get odd numbers - using 'filter' & 'lambda'   
def is_odd(values):  
    return filter(lambda x: x % 2, values)  

# calc function to convert from celsius to fahrenheit - using 'map'       
def to_fahrenheit(values):
    return map(fahrenheit, values)

# calc function to convert from fahrenheit to celsius - using 'map'   
def to_celsius(values):
    return map(celsius, values)

# calc function to get list of Fibonacci numbers up to 'n' - using 'list generator'
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n): return
        yield a
        a, b = b, a + b
        counter += 1
        
# alternative function to convert from celsius to fahrenheit - using 'list comprehension'    
def to_fahrenheit_alt_method(cel): 
    Fahrenheit = [ ((float(9)/5)*x + 32) for x in cel ]
    return Fahrenheit  
    
# alternative function to convert from fahrenheit to celsius- using 'list comprehension'
def to_celsius_alt_method(fahr):  
    Celsius = [ (float(5)/9)*(x -32) for x in fahr ]
    return Celsius      


# below are function calls to invoke the functions are print results
    
import os
os.system('cls')

print "\nCalling function 'Max'\n======================"
print "Numbers are: {}".format(num_list1)
print "Result = {}".format(max(num_list1))

print "\nCalling function 'Min'\n======================"
print "Numbers are: {}".format(num_list1)
print "Result = {}".format(min(num_list1))

print "\nCalling function 'Add'\n======================"
print "Numbers are: {}".format(num_list1)
print "Result = {}".format(add(num_list1))

print "\nCalling function 'Subtract'\n==========================="
print "Numbers are: {}".format(num_list1)
print "Result = {}".format(subtract(num_list1))

print "\nCalling function 'Multiply'\n==========================="
print "Numbers are: {}".format(num_list1)
print "Result = {}".format(multiply(num_list1))

print "\nCalling function 'Divide'\n========================="
print "Numbers are: {}".format(num_list2)
print "Result = {}".format(divide(num_list2))
print "Numbers are: {}".format(num_list3)
print "Result = {}".format(divide(num_list3))
print "Numbers are: {}".format(num_list4)
print "Result = {}".format(divide(num_list4))

print "\nCalling function 'Is Even'\n=========================="
print "Numbers are: {}".format(num_list)
print "Result = {}".format(is_even(num_list))

print "\nCalling function 'Is Odd'\n========================="
print "Numbers are: {}".format(num_list)
print "Result = {}".format(is_odd(num_list))

print "\nCalling function 'To Celsius'\n============================="
print "Temps to convert are: {}".format(fahrenheit_temps)
print "Result = {}".format(to_celsius(fahrenheit_temps))

print "\nCalling function 'To Fahrenheit'\n================================"
print "Temps to convert are: {}".format(celsius_temps)
print "Result = {}".format(to_fahrenheit(celsius_temps))

print "\nCalling ALTERNATIVE function 'To Celsius'\n========================================="
print "Temps to convert are: {}".format(fahrenheit_temps)
print "Result = {}".format(to_celsius_alt_method(fahrenheit_temps))

print "\nCalling ALTERNATIVE function 'To Fahrenheit'\n============================================"
print "Temps to convert are: {}".format(celsius_temps)
print "Result = {}".format(to_fahrenheit_alt_method(celsius_temps))

print "\nCalling function 'Fibonacci'\n============================"
f = fibonacci(50)
for x in f:
    print x,
print  



