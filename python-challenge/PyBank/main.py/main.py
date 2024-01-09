print("Financial Analysis")

print("--------------------------------------------------")

# import os module
import os
import csv

# Path to collect data from the Resources folder
totals_csv = os.path.join('..', 'Resources', 'budget_data.csv')

total_dates = []
# Read in CSV file
with open(totals_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through data
    for row in csvreader:
        total_dates = sum(1 for row[0] in csvreader)
        print(f'Total Months: {total_dates}')

# Set variables
Date_changes = total_dates - 1
total_prof = []
# Read in CSV file
with open(totals_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Loop through data
    for row in csvreader:
        total_prof = sum(int(row[1]) for row in csvreader)

        print(f'Total: ${total_prof}')

# Set variable for change list
change_list = []

# Read in CSV file
with open(totals_csv, 'r') as csvfile:

 # Split the data on commas and assign initial values
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    prev_value = int(first_row[1])

    # Loop through data
    for row in csvreader:
       
       change = int(row[1]) - prev_value

       prev_value = int(row[1])

       # Append change value to list
       change_list.append(change)

# Calculate sum of changes
total_change = sum(change_list)

# Calculate Avg
avg_change = round(total_change / Date_changes, 2)

print(f'Average Change: {avg_change}')

# Create Index Lists
Date = []
Profit_loss = []

# Read CSV file
with open(totals_csv, 'r') as csvfile:

 # Split the data on commas and assign initial values
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)

    for row in csvreader:

        # Append lists
        Date.append(row[0])
        Profit_loss.append(row[1])

# Zip list together
new_csv = list(zip(Date, Profit_loss, change_list))

# Set variable for output file
output_file = os.path.join('budget_data_final.csv')

# Open output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write header row
    writer.writerow(["Date", "Profit/Losses", "Change"])

    # Write in zipped rows
    writer.writerows(new_csv)

# Set variable for min and max values
minval = min(change_list)
maxval = max(change_list)

# Set variable for new CSV file
new_file = os.path.join('budget_data_final.csv')

# Import math module
import math

# Read CSV file
with open(new_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 0
# Set Variables
    When = []
    maxValue = -math.inf

#Establish for loop
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            if float(row[2]) > maxValue:
                When, maxValue = row[0], float(row[2])
    # Print max
    print(f'Greatest Increase in Profits: {When} (${maxValue})')

# Read CSV file
with open(new_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    line_count = 0
# set variables
    Tiempo = []
    minValue = math.inf
# Establish for loop
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            if float(row[2]) < minValue:
                Tiempo, minValue = row[0], float(row[2])
    # Print min
    print(f'Greatest Decrease in Profits: {Tiempo} (${minValue})')

print_to_text = f""" Financial Analysis
-----------------------------------------
Total Months: {total_dates}
Total: ${total_prof}
Average Change: {avg_change}
Greatest Increase in Profits: {When} (${maxValue})
Greatest Decrease in Profits: {Tiempo} (${minValue})"""

file = open("Analysis.txt", "w")
file.write(print_to_text)
file.close()