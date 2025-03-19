#These are practice questions
#Date 3/4/2025
#1. DNA sequence manipuation
#Reverse complement of a DNA string
#Write a function that takes a DNA sequence as input and returns its reverse complement.
def reverse_complement(dna: str) -> str:
    """
    Given a DNA sequence, return its reverse complement.
    A <-> T, C <-> G
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'
                  }
    return "".join(complement[base] for base in reversed(dna))
    

# Example:
# Input: "ATCG"
# Output: "CGAT"
if __name__ == "__main__":
    dna_sequence = "ATGCATGC"
    result = reverse_complement(dna_sequence)
    print(f"Reverse complement: {result}")