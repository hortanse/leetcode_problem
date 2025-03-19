##1. Reverse complement
sequence = "AAGGCTTGCCTTCCGGGATTACGG"

def reverse_complement(dna):
    complement = { #define complement dictionary
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join(complement[base] for base in reversed(dna))
print(sequence)
print(reverse_complement(sequence))

#2. GC content in FASTA
#read in a FASTA file
#calculate the GC content for each sequence
#Output sequence ID and its cooresponding GC content %\
sequence = "ATGCGCGATCGTGGTCCAA"
def gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100 if seq else 0

print(f"GC content: {gc_content(sequence):.2f}%")

##Parse in a FASTA file (without Biopython)
def read_fasta(file_path):
    #Read in a FASTA file and returns a dictionary of {sequence_id: sequence}
    sequences = {}
    with open(file_path, "r") as file:
        sequence_id = None
        sequence = []

        for line in file:
            line = line.strip()
            if line.startswith(">"): #new sequence header
                if sequence_id:
                    sequences[sequence_id] = "".join(sequence)
                sequence_id = line[1:] #remove '>'
                sequence = []
            else:
                sequence.append(line)
        if sequence_id: #store the last sequence
            sequences[sequence_id] = "".join(sequence)
    return sequences

##2. Other way to do using defaultdict
from collections import defaultdict
def parse_fasta(file_path):
    sequence = defaultdict(str)
    with open(file_path, 'r') as f:
        current_id = None #Keeps track of the current sequence ID
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:] #extract sequence ID (remove '>')
            elif current_id is not None:
                sequence[current_id] += line #Append sequence lines to the ID
    return sequence

## 3. Using Biopython
from Bio import SeqIO

def read_fasta_biopython(file_path):
    """Reads a FASTA file and returns a dictionary of {sequence_id: sequence} using Biopython"""
    return {record.id:str(record.seq) for record in SeqIO.parse(file_path, "fasta")}

#Example usage
fasta_file = "example.fasta"
sequences = read_fasta_biopython(fasta_file)
for seq_id, seq in sequences.items():
    print(f"{seq_id}: {seq}")

