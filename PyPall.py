# Add our dependencies
import csv
from email import header
import os
# Assign a variable to load a file form a path
file_to_load = ("/Users/szk/Desktop/Analysis Projects/Module 3 Python/Election_Analysis/Resources/election_results.csv")
# Assign a variable to load a file form a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#print(file_to_load)
# Open the eletion results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
