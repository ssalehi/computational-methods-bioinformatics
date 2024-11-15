import string
import sys

def detect_nucleotide_bases(str):
   adenine = 0
   thymine = 0
   cytosine = 0
   guanine = 0
   junkLetter = 0
   
   for ch in str:
    if ch=='A' or ch=='a':
         adenine = adenine+1
    elif ch=='T' or ch=='t':
        thymine = thymine+1
    elif ch=='C' or ch=='c':
        cytosine = cytosine+1
    elif ch=='G' or ch=='g':
        guanine = guanine+1
    else:
        junkLetter= junkLetter+1
   
   return(adenine, thymine, cytosine, guanine, junkLetter)


DNASeq = input("Enter DNA Sequence: ")

print(f"DNA_seq : {DNASeq}") 
print(f"It is {len(DNASeq)} bases long")
x= detect_nucleotide_bases(DNASeq)

    
print(f"adenine : {x[0]}")
print(f"thymine : {x[1]}")
print(f"cytosine : {x[2]}")
print(f"guanine : {x[3]}")
print(f"junkLetter : {x[4]}")