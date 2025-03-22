"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
"""


def parse_fasta(fasta_string):
    # Parse FASTA format string into a dictionary of sequences
    sequences = {}
    current_id = None
    current_seq = []

    # Split the input string into lines and process each line
    for line in fasta_string.strip().split('\n'):
        if line.startswith('>'):  # This is a header line
            if current_id:  # save the previous sequence if it exists
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:]  # Remove the '>' from the ID
            current_seq = []  # reset for the new sequence
        else:
            current_seq.append(line)
    # Don't forget to save the last sequence
    if current_id:
        sequences[current_id] = ''.join(current_seq)
    return sequences


def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_length = len(sequence)
    return (gc_count/total_length) * 100 if total_length > 0 else 0


def find_highest_gc_content(fasta_string):
    # parse the FASTA string
    sequences = parse_fasta(fasta_string)

    # Calculate GC content for each sequence
    gc_contents = {
        seq_id: calculate_gc_content(seq) for seq_id, seq in sequences.items()
    }
    # Find the sequence with maximum GC content
    max_gc_id = max(gc_contents, key=gc_contents.get)

    return max_gc_id, gc_contents[max_gc_id]


# Test sample dataset
sample_dataset = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

# Get and print results
seq_id, gc_content = find_highest_gc_content(sample_dataset)
print(seq_id)
print(f"{gc_content:.6f}")
