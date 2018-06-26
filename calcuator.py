# Francis Oludhe
# Simple Calculator

import time
import sys

# Operations to be used in the equation
operations = ['1', '2','3', '4']

# List of the related keys and operations
print ('Operation keys.')
print ('\n1 - Add')
print ('2 - Subtract')
print ('3 - Multiply')
print ('4 - Divide')

# Equations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Input
a = int(input("\nKindly input your first value? "))

value = input("\nPick between 1, 2, 3, 4? ")

while value not in operations:
    print ("\nPlease anser with 1, 2, 3, 4?")
    value = int(input("\nPick between 1 for addition and 2 for subtraction? "))

b = int(input("\nKindly input your second value? "))

# The bulk of the equation
if value == '1':
    print('\n', a, '+', b, '=', add(a, b))
    print('')
    time.sleep(2)
    sys.exit

elif value == '2':
    print('\n', a, '-', b, '=', subtract(a, b))
    print('')
    time.sleep(2)
    sys.exit

elif value == '3':
    print('\n', a, 'x', b, '=', multiply(a, b))
    print('')
    time.sleep(2)
    sys.exit

elif value == '4':
    print('\n', a, '/', b, '=', divide(a, b))
    print('')
    time.sleep(2)
    sys.exit

else:
    print('\nInvalid Input')
    time.sleep(2)
    sys.exit
