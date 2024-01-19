# Math Calculator
# Importing the math module

import math
# Function to add two numbers
def add(x, y):
  return x + y
  
# Function to subtract two numbers
def subtract(x, y):
  return x - y

# Function to multiply two numbers
def multiply(x, y):
  return x * y

# Function to divide two numbers
def divide(x, y):
  return x / y

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating \
            with {answer}, or type 'n' to start a \
                        new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
