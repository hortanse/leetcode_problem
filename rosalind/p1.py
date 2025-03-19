"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
20 12 17 21
"""
def count_necleotides(dna_string):
    a_count = dna_string.count('A')
    c_count = dna_string.count('C')
    g_count = dna_string.count('G')
    t_count = dna_string.count('T')
    #return the counts as a string with space separation
    return f"{a_count} {c_count} {g_count} {t_count}"

#Test with the sample dataset
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(count_necleotides(dna))

"""
Alternate solution
Use Dictionary or Counter from collections
"""
from collections import Counter

def count_necleotides_alt(dna_string):
    #Count all nucleotides using Counter
    counts = Counter(dna_string)

    #return counts in required order
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(count_necleotides_alt(dna))