# Name: Paul Prew
# Student Number: 10354828
# Programming for Big Data
# CA 1


# The following is a calculator program which includes basic calculation functions 
# and also a selection of scientific functions. When the program opens the user will 
# be asked to enter the first number. The user is then presented with a list of 
# operators and is asked to select one of these. After the operator has been selected
# the user will be asked to enter a second number if this is required, as depends on 
# the chosen operator.  
# The program will then compute the result, and output the calculation and result to
# the screen.
# The user is then prompted if they wish to do a abother calculation, or exit the program.
# On exiting the program, the calculation and results are saved to a txt file named 
# archive_results.txt.
# This program calls a separate script named 'functions_calculator.py' which includes the 
# functions for doing the calculations.


from functions_calculator import *

import os

operators_menu = {1:'add',2:'subtract',3:'multiply', 4:'divide',5:'exponent',6:'square root',7:'square',8:'cube',9:'sine',10:'cosine'}
results = list()

def getfloatinput(user_prompt) :
    while True:
        try: 
            str_num = raw_input(user_prompt)
            num = float(str_num) 
            return num
        except :
            print 'Invalid entry! Entry be a numeric value.'
            continue    

def get_operator() :
    menu_list = operators_menu.items()
    menu_list.sort()
    print ''
    for key, val in menu_list: 
        print "# Select '{}' to use the {} operator".format(key,val)
          
    while True:
        choice = raw_input()
        if choice not in str(operators_menu.keys()):
            print 'Invalid Selection. Try again!'
            continue
        else :
            return int(choice)   

            
# main program
while True :
    os.system('cls')

# display program name and get user inputs for calculation
    print 'Scientific Calculator\n---------------------'
    num1 = getfloatinput('\nEnter first number: ')
    choice_operator = get_operator()

    if choice_operator in (1,2,3,4,5):
        num2 = getfloatinput('\nEnter second number: ')
        if choice_operator == 1 : result = calc_add(num1,num2)
        elif choice_operator == 2 : result = calc_subtract(num1,num2)
        elif choice_operator == 3: result = calc_multiply(num1,num2)
        elif choice_operator == 4 : result = calc_divide(num1,num2)
        elif choice_operator == 5 : result = calc_exp(num1,num2)    
        
    else :
        num2 = ""
        if choice_operator == 6 : result = calc_squareroot(num1)
        elif choice_operator == 7 : result = calc_square(num1)
        elif choice_operator == 8 : result = calc_cube(num1)
        elif choice_operator == 9 : result = calc_sine(num1)
        elif choice_operator == 10 : result = calc_cosine(num1)

# display results of calculation        
    print '\n\nCalculation Results\n-------------------'
    if num2 == "" :
        print operators_menu[choice_operator], 'of', num1, '\tequals\t', result
    else :
        print num1, operators_menu[choice_operator], num2, '\tequals\t', result

# store calculation and results        
    transaction = [num1, operators_menu[choice_operator],num2, result]
    results.append(transaction)   
    
# prompt user for next action    
    print "\n\nEnter 'C' to do another calculation." 
    print "Enter any other key to quit. Reseults will be saved to txt file."  
    next_action = raw_input().lower()
    if next_action == 'c' :
        continue
    else :
        break         
        
# write calculation results to text file
try : 
    text_file = "archive_results.txt"
    f = open(text_file, "a")
    for item in results:
        f.write(str(item) + "\n")
    f.close()       
    print '\nExport to filename {} was successfull.'.format(text_file)
except :
    print '\nExport to filename {} was not successfull!'.format(text_file)
    
