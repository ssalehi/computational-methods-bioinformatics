import string
import sys

def prnt_str(str):
    for i in range (10):
        print(f"{i}: {str}")


def restriction_site_patterns (myList):
    myStr= " is a restriction sit"
    for el in myList:
        text= el+myStr
        print(f"{text}")

def check_seq(str, myList):
    for el in myList:
        print(f"{el} is in the {str} : {el in str}")


myStr = input("Enter your string: ")
prnt_str(myStr)
print(f"**********************************")

restriction_list = ['GAATTC','GGATCC','AAGCTT']
restriction_site_patterns(restriction_list)
print(f"**********************************")

enterdSeq = input("Enter the sequence: ")
check_seq(enterdSeq, restriction_list)

