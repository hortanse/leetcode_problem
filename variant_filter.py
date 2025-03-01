##You have a VCF file containing genetic variants. Write a Python function to filter out variants where the QUAL (quality score) is below 30.
#Example Input (variants.vcf)
##CHROM POS ID REF ALT QUAL FILTER
#chr1 12345 rs1 A T 50 PASS
#chr1 67890 rs2 C G 20 LOW_QUAL
#chr2 11111 rs3 G A 45 PASS
# Expected Output:
#chr1 12345 rs1 A T 50 PASS
#chr2 11111 rs3 G A 45 PASS
#My approach
#1. Read in the vcf file
#2. filter out low QUAL < 30
#3. Output a new vcf file

def filter_vcf(input, output, qual_threshold=30):
    with open (input, 'r') as infile, open(output, 'w') as outfile:
        for line in infile:
            if line.startswith("#"): #keep metadata/header lines
                outfile.write(line)
                continue
            columns = line.strip().split("\t")
            try: #add error handling
                qual = float(columns[5]) #QUAL is column index 5
                if qual >= qual_threshold:
                    outfile.write(line)
            except (IndexError, ValueError):
                print("Warning: Skipping malformed line: {line.strip()}")

if __name__ == "__main__":
    filter_vcf("input.vcf", "filtered.vcf", qual_threshold=30)
            