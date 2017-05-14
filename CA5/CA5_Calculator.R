# Name: Paul Prew
# Student Number: 10354828
# Programming for Big Data
# CA 5


# PROGRAM NOTES
#
# The following is a calculator program in R, which includes basic calculation 
# functions and also a selection of scientific functions. 
# The user starts the program execution by pressing keys 'Control + Shift + S'.
# A menu list of operators is then displayed in the console window, and the user is 
# asked to select one of the options numbered 1-10.
# Before selection, the user is required to click anywhere within the console window.
# The user then enters their choice of selection (1-10) and hits return.
# The user is then asked to enter one or two numbers depending on the operator they 
# have selected. The program will then compute the result, and output the result to 
# the console window.
# The user is then prompted if they wish to do a another calculation, or exit the program.


# FUNCTIONS
#
# The 10 calculator functions are defined below.
# These calculator functiuons are called in the main program, according to the choice of
# operator selected by the user.

# The add function accepts as parameters 2 numbers and computes the result
add <- function(num1, num2) {
    result <- num1 + num2
    return(result)
}

# The subtract function accepts as parameters 2 numbers and computes the result
subtract <- function(num1, num2) {
    result <- num1 - num2
    return(result)
}

# The multiply function accepts as parameters 2 numbers and computes the result
multiply <- function(num1, num2) {
    result <- num1 * num2
    return(result)
}

# The divide function accepts as parameters 2 numbers and computes the result
# The function includes an error message if the user enters division by 0.
divide <- function(num1, num2) {
  calc <- num1 / num2
  if (is.infinite(calc)) {
    result <- "Error: Cannot Divide by Zero!"
  }
  else {result <- calc
    }
  return(result)
}

# The exponent function accepts as parameters 2 numbers and computes the result
exponent <- function(num1, num2) {
    result <- num1 ** num2
    return(result)
}

# The square root function accepts 1 number parameter and computes the result.
# The function includes an error message if the user enters a negative number.
square_root <- function(num) {
  calc <-(sqrt(num))
  if (is.nan(calc)) {
    result <-"Number Error!"
  }
  else {result <- calc
  }
  return(result)
}

# The square function accepts 1 number parameter and computes the result.
# This function makes a call to another function 'exponent' with a parameter of 2.
square <- function(num) {
  result <- exponent(num, 2)
  return(result)
}

# The cube function accepts 1 number parameter and computes the result.
cube <- function(num) {
  result <- exponent(num,3)
  return(result)
}

# The sine function accepts 1 number parameter (degrees) and computes the result.
# The function specifies exception results e.g. 
# where degrees = 180 or 360 then sine(degrees) is 0.  
sine <- function(deg){
  if (deg %% 180 == 0) {
  result <- 0
  }
  else {
    result <- sin(deg*(pi/180))
  }
  return(result)
}

# The cosine function accepts 1 number parameter (degrees) and computes the result.
# The function specifies exception results e.g. 
# where degrees = 90 or 270 then cosine(degrees) is 0      
cosine <- function(deg) {
  if ((deg - 90) %% 180 == 0) {
    result <- 0
  }
  else {result <- cos(deg*pi/180)
  }
  return(result)
}


# MAIN PROGRAM
#
# While loop included which will loop back to the main menu after the user has
# completed a calculation and selects to enter another.
#
while (TRUE) {
  cat("\014") 
  print("Calculator")
  print("==========")
  print("Select operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Exponent")
  print("6.Square Root")
  print("7.Square")
  print("8.Cube")
  print("9.Sine")
  print("10.Cosine")
  
  # While loop included which will not progress until a valid menu number is selected
  while (TRUE) { 
    choice = as.numeric(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))
    if (!choice %in% c('1','2','3','4','5','6','7','8','9','10')) {
      print("Invalid selection! Please try again")
    }
    else {break    } 
  }
  
  # User is prompted to select numbers for calculation.  If statement ensures user is 
  # only asked for 2nd number when necessary
  num1 = as.numeric(readline(prompt="Enter first number: "))
  if (choice <= 5) {
    num2 = as.numeric(readline(prompt="Enter second number: "))
  }
  
  # switch function will map the choice operator selected by the user to the relevant
  # calculator function
  operator <- switch(choice,"+","-","*","/","Exponent", "Square Root","Square","Cube","Sine","Cosine")
  result <- switch(choice, 
    add(num1, num2), 
    subtract(num1, num2), 
    multiply(num1, num2), 
    divide(num1, num2),
    exponent(num1, num2),
    square_root(num1),
    square(num1),
    cube(num1),
    sine(num1),
    cosine(num1))
  
  # Result of calculation is printed to console
  if (choice <= 5) {
    print(paste(num1, operator, num2, "=", result))
  }
  else {
    print(paste(operator, "of", num1, "=", result)) 
  }
  
  # User is prompted if they wish to enter another calculation or exit program
  str = readline(prompt="Enter another calculation: Y/N")
  str = tolower(str)
  if (str == 'y') {next
  }
  else {break
  }
}


