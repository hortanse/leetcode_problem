#1. DNA nucleotide counting
#key concept: string manipulation, dictionaries
def count_nucleotides(dna):
    return {'A' : dna.count('A'), 'T' : dna.count('T'), 'G' : dna.count('G'), 'C' :dna.count('C')}

#2. Reserve complement of DNA
#key concept: string reversal, dictionary mapping
def reverse_complement(dna):
    complement = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    return ''.join([complement[nt] for nt in reversed(dna)])
#example usage
dna = "ATGC"
print(reverse_complement(dna))

#3. Translation DNA to Protein
#Convert a DNA sequencing into a protein using the genetic code (codon table)
#key concept:condon mapping, slicing, loops
def dna_to_protein(dna):
    codon_table = {"TTT" : "F", "TTC" : "F", "TTA" : "L", ....} #truncated for brevity
    protein = []
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        protein.append(codon_table.get(codon, "*"))
    return ''.join(protein)
#4. Finding Mofit in DNA
#Identify all starting positions of a motif(substring) in a DNA sequence
#key concept: sliding winwdow, string indexing
def find_motif(dna, motif):
    return [i+1 for i in range(len(dna)-len(motif) +1) if dna[i:i+len(motif)] == motif]
#5. GC content calculation
#compute the GC content in a DNA sequence
#key concept: string iteration, basic statistics
def gc_content(dna):
    gc = dna.count('G') + dna.count('C')
    return (gc / len(dna)) * 100 if dna else 0
#6 FASTA file parsing
#Read a FASTA file and return a dictionary mapping sequencing IDs to DNA/protein sequences
#key concept: File I/O, string manipulation
def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as f:
        current_id = None #initialize as None instead of empty string
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:] #remove '>' and store the ID
                sequences[current_id] = "" #Initialize empty sequence for this ID
            elif current_id is not None: #only add sequence if we have an ID
                sequences[current_id] += line
    return sequences
#7. Codon usage bias
#calculate the frquency of each codon for a given amino acid
#frequency counting, codon tables
def codon_bias(protein_sequence, target_aa):
    codon_table = {"CTT": "L", "CTC": "L", ... }  # Example codon table
    codons = []
    #check input parameters
    if not dna_sequence or not target_aa:
        return {}
    
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        if codon_table.get(codon) == target_aa:
            codons.append(codon)
    return {codon : codons.count(codon) for codon in set(codons)}

#8. K-mer counting
#count all overlapping k-mers(substrings of length k) in a DNA sequence
#key concept: sliding window, dictionaries
def count_kmers(dna, k):
    kmers = {}
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        kmers[kmer] = kmers.get(kmer, 0) +1
    return kmers

#9. Sequence alignment(Needleman-Wunsch)
#Implement a global sequence alignment algorithm with a given scoring matrix
#Key concept: Dynamic programming, matrices
def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    # Initialize matrix
    n, m = len(seq1), len(seq2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    # Fill matrix (simplified example)
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = gap * max(i, j)
            else:
                match_score = dp[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
                dp[i][j] = max(match_score, dp[i-1][j] + gap, dp[i][j-1] + gap)
    return dp[n][m]

#10. Generating all possible mRNA sequence from a protein
#Given a protein sequence, generate all possible mRNA sequences that could encode it
#key concept: recursion, backtracking, combinaatorics

from itertools import product

def generate_mrna(protein):
    codon_table = {"F": ["TTT", "TTC"], "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"], ... }  # Simplified
    mrna_options = [codon_table[aa] for aa in protein]
    return [''.join(combination) for combination in product(*mrna_options)]

