import string
import sys

#def detect_nucleotide_bases(str):   
   #return(str.count("A"),str.count("T"), str.count("C"),str.count("G"))


DNASeq = input("Enter DNA Sequence: ")

print(f"DNA_seq : {DNASeq}") 
print(f"It is {len(DNASeq)} bases long")

x=DNASeq.count("A")+DNASeq.count("a")
y=DNASeq.count("T")+DNASeq.count("t")
w=DNASeq.count("C")+DNASeq.count("c")
z=DNASeq.count("G")+DNASeq.count("g")
print(f"adenine : {x}")
print(f"thymine : {y}")
print(f"cytosine : {w}")
print(f"guanine : {z}")