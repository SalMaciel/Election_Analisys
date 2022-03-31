# Data we need to retrive
# 1 Total number of votes cast
# 2 A complete list with candid names
# 3 Percentage of votes each candidate got
# 4 Total number of votes each condidate got
# 5 Winner of the election by popular vote
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    



    
    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)




# Close the file.
# election_data.close()
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis","election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")
