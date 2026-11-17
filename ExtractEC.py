#!/home/proteinmechanic/local/anaconda3/bin/python

import os, sys, glob, subprocess
from tqdm import tqdm 
import numpy as np

# Define input and output file paths
input_file_path = sys.argv[1]
output_file_path = sys.argv[1].split('.')[0] + '.out'

# Open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Initialize variables to store ID and DR values
    current_id = None
    dr_values = []

    # Iterate through lines in the input file
    for line in input_file:
        line = line.strip()
        # Check if the line starts with "ID"
        if line.startswith("ID"):
            # If there was a previous ID, write it and the DR values to the output file
            if current_id is not None:
                output_file.write(f"{current_id}\t{'; '.join(dr_values)}\n")
            # Extract the new ID
            current_id = line.split()[1]
            dr_values = []
        # Check if the line starts with "DR"
        elif line.startswith("DR"):
            # Extract the DR value and add it to the list
            dr_value = line.split()[1]
            dr_values.append(dr_value)

    # Write the last ID and DR values to the output file
    if current_id is not None:
        output_file.write(f"{current_id}\t{'; '.join(dr_values)}\n")

print("Conversion completed.")
