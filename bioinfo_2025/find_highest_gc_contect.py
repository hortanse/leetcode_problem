###
#Given a FASTA file containing multiple DNA sequences, write a Python script to find the sequence with the highest GC content.
#Example Input (fasta.txt)
#>seq1
#ATGCGCGATCGT
#>seq2
#ATATATATATA
#>seq3
#GCGCGCGCGCGA
#Expected Output:
#seq3 (GC Content: 91.67%)
#My approach for this 1. Read in a fasta.txt file
# 2. calculate the GC contect for each sequence
# 3. compare them to get the highest one
from collections import defaultdict

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100 if seq else 0

def parse_fasta(file_path):
    sequence = defaultdict(str)
    with open(file_path, 'r') as f:
        current_id = None
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
            elif current_id is not None:
                sequence[current_id] += line
    return sequence

def find_highest_gc(file_path):
    sequences =  parse_fasta(file_path)
    if not sequences:
        print("No sequences found in the file")
        return
    
    max_gc = 0
    max_seq_id = None

    for seq_id, seq in sequences.items():
        gc_cont = gc_content(seq)
        if gc_cont > max_gc:
            max_gc = gc_cont
            max_seq_id = seq_id
    print(f"{max_seq_id} (GC content: {max_gc:.2f}%)")

if __name__ == "__main__":
    find_highest_gc("fasta.txt")