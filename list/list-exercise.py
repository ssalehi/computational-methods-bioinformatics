import string
import sys


def make_list(str):
   myList = str.split()
   return(myList)

seperatedWords = input("Enter 2 seperated word with a single space between: ")
print(f"You entered : {seperatedWords}") 

result = make_list(seperatedWords)
print(result)