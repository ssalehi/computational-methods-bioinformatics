import string
import sys

def calc_factorial(n):
    nFactorial = 1
    for i in range (n):
        nFactorial = nFactorial*(i+1)

    return nFactorial

myNumber = int(input("Enter the Number to calculate its factorial: "))
print(f"factorial of {myNumber} is {calc_factorial(myNumber)}")
print(f"**********************************")