import string
import sys

seperatedWords = input("Enter 2 seperated word with a single space between: ")
print(f"You entered : {seperatedWords}") 

#myList = str.split(seperatedWords)
#I would not use the static reference "str.split()" but instead make directly use of your String variable "seperatedWords". For better understanding, I recommend asking Professor Lanese, since I didn't find a good explanation.
myList = seperatedWords.split()
print(f"{myList[0]}, {myList[1]}")