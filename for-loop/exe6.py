import string
import sys

restriction_list = ['GAATTC','GGATCC','AAGCTT']
print(f"The list is:[\'{restriction_list[0]}\',\'{restriction_list[1]}\',\'{restriction_list[2]}\']")
myStr= " is a restriction sit"
for el in restriction_list:
    text= el+myStr
    print(f"{text}")
print(f"**********************************")


