##You have a CSV file containing gene expression data. Write a Python script to normalize all expression values using the formula:
#normalized = [(x - min_x) / (max_x - min_x)
#Example Input (gene_expression.csv)
#Gene,Expression
#TP53,200
#BRCA1,150
#EGFR,400
#MYC,300
#Expected Output:
#Gene,Normalized_Expression
#TP53,0.1667
#BRCA1,0.0
#EGFR,1.0
#MYC,0.5

#My approach is
#1. Read in a file and get expression value
#2. calculate normalized values
#3. output a file with normalized values
import pandas as pd

def normalized_expression(input_csv, output_csv):
    try:
        df = pd.read_csv(input_csv)

        if "Expression" not in df.columns:
            raise ValueError("Input csv must contain 'Expression' column")
    #Min-Max Normalization Formula: (x - min) / (max - min)
        min_expr = df["Expression"].min()
        max_expr = df["Expression"].max()

        if max_expr == min_expr:
            raise ValueError("Cannot normalize: all expression values are identical")
    
        df["Normalized_Expression"] = (df["Expression"] - min_expr) / (max_expr - min_expr)
        #select only 'Gene' and 'Normalized_Expression' for output
        df = df[["Gene", "Normalized_Expression"]]
        
        df.to_csv(output_csv, index=False)
    except pd.errors.EmptyDataError:
        print("Error: Input CSV file is empty")
    except FileExistsError:
        print("Error: Could not find input file '{input_csv}'")
    except ValueError as e:
        print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    normalized_expression("gene_expression.csv", "normalized_expression.csv")

