#import string
#import sys

#seperatedWords = input("Enter seperated words with spaces between them: ")
#print(f"You entered : {seperatedWords}") 
#myList = str.split(seperatedWords)
#print(myList)

import string
import sys

seperatedWords = input("Enter seperated words with spaces between them: ")
print(f"You entered : {seperatedWords}") 
x = seperatedWords.count(" ")
y = seperatedWords.find(" ")