import string
import sys

seperatedWords = input("Enter 2 seperated word with a single space between: ")
print(f"You entered : {seperatedWords}") 

myList = str.split(seperatedWords)
print(f"{myList[0]}, {myList[1]}")