import pandas as pd
import argparse

def remove_column(input_file, output_file, column_name):
    # Load the OTU table
    otu_table = pd.read_csv(input_file, sep='\t')
    
    # Check if the column exists in the table
    if column_name in otu_table.columns:
        # Drop the specified column
        otu_table_updated = otu_table.drop(columns=[column_name])
        # Save the updated OTU table to a new file
        otu_table_updated.to_csv(output_file, sep='\t', index=False)
        print(f"Column '{column_name}' removed and saved to '{output_file}'.")
    else:
        print(f"Column '{column_name}' not found in the OTU table.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Remove a specific column from an OTU table.')
    parser.add_argument('-i', '--input', required=True, help='Input OTU table file (TSV format).')
    parser.add_argument('-o', '--output', required=True, help='Output OTU table file after removing the column.')
    parser.add_argument('-c', '--column', required=True, help='Column name to remove.')

    # Parse arguments
    args = parser.parse_args()

    # Call the function to remove the column
    remove_column(args.input, args.output, args.column)

