##List comprehensions are useful for handling large bioinformatics datasets efficiently. Here are some Python practice problems:

#1. Extract all gene names from a list of dictionary records:
##if we only want genes longer than 800bp, we can add an if condition:
genes = [{'name': 'BRCA1', 'length': 1200}, {'name': 'TP53', 'length': 900}, {'name': 'MYC', 'length': 750}]
gene_names = [ gene['name'] for gene in genes if gene['length'] > 800]
print(gene_names)

#Task: Extract only the gene names into a list using list comprehension.

#2. Filter FASTQ reads that have a minimum quality score:
reads = [("ATCG", 30), ("GCTA", 25), ("TATA", 35), ("GGGG", 20)]
#min_quality = [ min(read[1]) for read in reads]
filtered_reads = [ read for read in reads if read[1] >= 30]
print(filtered_reads)

#Task: Extract sequences where the quality score is ≥30.

#3. Convert a list of DNA sequences to RNA (replace 'T' with 'U'):
sequences = ["ATGC", "TATA", "GCGC", "TTAA"]
RNA_seq = [sequence.replace('T', 'U') for sequence in sequences]
print(RNA_seq)

#Task: Convert all sequences to RNA using list comprehension.

#4. Calculate GC content for a list of DNA sequences:

sequences = ["ATGC", "CCGG", "TTAA", "GCGC"]
GC_content = [ (sequence.count('G') + sequence.count('C')) / len(sequence) for sequence in sequences]
print(GC_content)

#Task: Compute GC content (%) for each sequence using list comprehension.

#5. Extract gene IDs from GTF-like annotations:

annotations = ["gene_id ENSG000001; gene_name BRCA1;", "gene_id ENSG000002; gene_name TP53;"]
gene_id = [ annotation.split(" ")[1].rstrip(";") for annotation in annotations]
print(gene_id)

#Task: Extract only the gene IDs into a list.

#6. Find all genes longer than 1000 base pairs:
genes = [{'name': 'BRCA1', 'length': 1200}, {'name': 'TP53', 'length': 900}, {'name': 'MYC', 'length': 750}, {'name': 'EGFR', 'length': 1100}]
#Task: Extract gene names where length > 1000 using list comprehension.
gene_name = [gene['name'] for gene in genes if gene['length'] > 1000]
print(gene_name)

#7. Extract unique bases from a DNA sequence (no duplicates):
sequence = "AAGGCTTGCCTT"
#Task: Extract unique bases into a list without duplicates.
unique_sequence = list(set(sequence))
print(unique_sequence)

#8. Convert a list of tuples (chromosome, position) into a dictionary:
variants = [("chr1", 12345), ("chr2", 67890), ("chrX", 54321)]
#Task: Convert into a dictionary where chromosome is the key, and position is the value.
#tuple_2_dict = [ { chr: pos }  for chr, pos in variants] # this will create a list of dictionaries not a single dictionary
tuple_2_dict = {chr:pos for chr, pos in variants}
print(tuple_2_dict)

#9. Convert a list of amino acids to their corresponding codons:

amino_acids = ['M', 'A', 'T', 'G']
codon_table = {'M': 'ATG', 'A': 'GCG', 'T': 'ACT', 'G': 'GGT'}
#Task: Use list comprehension to convert each amino acid to its codon.

convert = [ codon_table[aa] for aa in amino_acids]
print(convert)

#10. Find all palindromic sequences in a list of DNA sequences:
sequences = ["ATGCAT", "TATA", "GCGC", "AAGG"]
##Task: Extract only the sequences that are palindromes.
#If reverse string match to the original string the string is palindrome
#palin_seq = [seq for seq in sequences if seq == seq[::-1]]
palin_seq = [seq for seq in sequences if seq == seq[::-1]]
print(palin_seq)
for seq in sequences:
    print(f"Original: {seq}' -> Reserved: '{seq[::-1]}' -> Match: {seq == seq[::-1]}")