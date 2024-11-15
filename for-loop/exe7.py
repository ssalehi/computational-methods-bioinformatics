import string
import sys

restriction_list = ['GAATTC','GGATCC','AAGCTT']
enterdSeq = input("Enter the sequence: ")

for el in restriction_list:
    print(f"{el} is in the {enterdSeq} : {el in enterdSeq}")


