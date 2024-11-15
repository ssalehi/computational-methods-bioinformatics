import string
import sys


def check_seq(str, myList):
    for el in myList:
        print(f"{el} is in the {str} : {el in str}")


restriction_list = ['GAATTC','GGATCC','AAGCTT']
enterdSeq = input("Enter the sequence: ")
check_seq(enterdSeq, restriction_list)

