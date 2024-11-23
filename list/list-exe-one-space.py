import string
import sys

seperatedWords = input("Enter 2 seperated words with a single spaces between them: ")
print("You entered : {seperatedWords}") 


x = seperatedWords.find(" ")

myList = [seperatedWords[:x], seperatedWords[x:]]
print(myList)