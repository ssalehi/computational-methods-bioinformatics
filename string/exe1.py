import string
import sys

#def detect_nucleotide_bases(str):   
   #return(str.count("A"),str.count("T"), str.count("C"),str.count("G"))


DNASeq = input("Enter DNA Sequence: ")

print(f"DNA_seq : {DNASeq}") 
print(f"It is {len(DNASeq)} bases long")
    
print(f"adenine : {DNASeq.count('A')}")
print(f"thymine : {DNASeq.count('T')}")
print(f"cytosine : {DNASeq.count('C')}")
print(f"guanine : {DNASeq.count('G')}")