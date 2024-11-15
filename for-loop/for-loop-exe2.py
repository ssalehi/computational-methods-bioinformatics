import string
import sys

def restriction_site_patterns (myList):
    myStr= " is a restriction sit"
    for el in myList:
        text= el+myStr
        print(f"{text}")



restriction_list = ['GAATTC','GGATCC','AAGCTT']
print(f"The list is:[\'{restriction_list[0]}\',\'{restriction_list[1]}\',\'{restriction_list[2]}\']")
restriction_site_patterns(restriction_list)
print(f"**********************************")


