"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u
.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t
.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""
def transcibe_dna_to_rna(dna):
    rna = dna.replace('T', 'U')
    return rna

#test
dna = "GATGGAACTTGACTACGTAAATT"
print(transcibe_dna_to_rna(dna))
    
"""
Alternate solution
Using a translation table or string maketrans
"""
def transcribe_rna_to_dna_alt(dna):
    #create a translation table
    trans_table = str.maketrans('T', 'U')
    #Transcribe DNA to RNA using translation table
    rna = dna.translate(trans_table)
    return rna