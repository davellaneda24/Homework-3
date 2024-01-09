print("Election Results")

print("--------------------------------------------------")

# Import OS module
import os
import csv

# Path to collect data from the Resources folder
ballot_csv = os.path.join('..', 'Resources', 'election_data.csv')

total_votes = []
# Read in CSV file
with open(ballot_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')


 # Loop through data
    for row in csvreader:
        total_votes = sum(1 for row[0] in csvreader)
        print(f'Total Votes: {total_votes}')

print("--------------------------------------------------")
# Read in CSV file
with open(ballot_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

# Set up vot counters for each candidate
    Charles_count = 0
    Diana_count = 0
    Raymon_count = 0

# Set Variables for candidate vote percentages
    C_percent = 0
    D_percent = 0
    R_percent = 0

# Loop through the data
    for row in csvreader:

        if row[2] == "Charles Casper Stockham":
            Charles_count += 1
        if row[2] == "Diana DeGette":
            Diana_count += 1
        if row[2] == "Raymon Anthony Doane":
            Raymon_count += 1
    
    # establish value for results
    Numbers = {"Charles Casper Stockham": Charles_count, "Diana Degette": Diana_count, "Raymond Anthony Doane": Raymon_count}

    C_percent = round((Charles_count / total_votes) * 100, 3)

    D_percent = round((Diana_count / total_votes) * 100, 3)

    R_percent = round((Raymon_count / total_votes) * 100, 3)

    # Print Results
    print(f'Charles Casper Stockham: {C_percent}% ({Charles_count} Votes)')
    print(f'Diana DeGette: {D_percent}% ({Diana_count} Votes)')
    print(f'Raymon Anthony Doane: {R_percent}% ({Raymon_count} Votes)')

print("--------------------------------------------------")

Winner = max(Numbers, key=Numbers.get)

print(f'Winner: {Winner}')

print("--------------------------------------------------")

print_to_text = f""" Election Results
-----------------------------------------
Total Votes: {total_votes}
-----------------------------------------
Charles Casper Stockham: {C_percent}% ({Charles_count} Votes)
Diana DeGette: {D_percent}% ({Diana_count} Votes)
Raymon Anthony Doane: {R_percent}% ({Raymon_count} Votes)
-----------------------------------------
Winner: {Winner}"""

print(print_to_text)

file = open("Analysis.txt", "w")
file.write(print_to_text)
file.close()