#import string
#import sys

#seperatedWords = input("Enter seperated words with spaces between them: ")
#print(f"You entered : {seperatedWords}") 
#myList = str.split(seperatedWords)
#print(myList)

import string
import sys

seperatedWords = input("Enter seperated words with spaces between them: ")
print(f"You entered : {seperatedWords}") #No need for f-string, since "seperatedWords" is a string. "input()" returns a String.#
#print("You entered :", seperatedWords) #Easier way of compilation (see explanation above).
x = seperatedWords.count(" ")
y = seperatedWords.find(" ")