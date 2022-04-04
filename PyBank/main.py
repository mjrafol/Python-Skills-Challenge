# Module for code to run across multiple systems.
import os

# Module for reading a csv file.
import csv

# Set path for the input csv file.
csvpath = os.path.join('Resources','budget_data.csv')

# Set list to store month, date, profit/loss and changes in profit/loss.
month = []
date = []
pl = []
change_list = []

# Set variables and initial value for total profit/loss, profit/loss change, and last period profit/loss change.
total = 0
pl_lastpd = 0
pl_totalchange = 0

# Open and read the csv file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store the header row.
    csvheader = next(csvreader)

    # Read through the records and calculate the analysis requirements.
    for row in csvreader:
        
        # Split the period and store month into a list.
        period = row[0].split("-")
        month.append(period[0])
        date.append(row[0])

        # Calculate the total profit/loss over the entire period.
        pl.append(int(row[1]))
        total = int(row[1]) + total

        # Assign value for current period.
        pl_currentpd = int(row[1])
         
        # Calculate change in profit/loss and assign value for the last period.
        pl_change = pl_currentpd - pl_lastpd
        change_list.append(pl_change)
        pl_lastpd = pl_currentpd
        pl_totalchange += pl_change
 
    # Return the months with the greatest increase and greatest decrease in profits.
    maxpl_index = change_list.index(max(change_list))
    minpl_index = change_list.index(min(change_list))

    # Bote that the solution excludes the change during the first period.  Set variable for the first period change.
    first_pdchange = change_list[0]

# Print the analysis data requirements.
print("Financial Analysis")
print("----------------------------")

# Total number of months included in the data set.
print(f"Total Months: {int(len(month))}")

# Net total amount of profit/loss over the entire period.
print(f"Total: ${(total)}")

# Changes in profit/loss over the entire period, and average of those changes.
print(f"Average Change: ${round(((pl_totalchange-first_pdchange)/(int(len(month))-1)),2)}")

# Greatest increase in profits (date and amount) over the entire period.
print(f"Greatest Increase in Profits: {date[maxpl_index]} (${(max(change_list))})")

# Greatest decrease in profits (date and amount) over the entire period.
print(f"Greatest Decrease in Profits: {date[minpl_index]} (${(min(change_list))})")

# Set path for the output csv file.
output_path = os.path.join('Analysis','PyBank_output.csv')

# Export a text file with the analysis table.
with open (output_path,'w') as csvoutput:

    # Initialize csvoutput writer.
    csvwriter = csv.writer(csvoutput,delimiter=',')

    # Write the analysis results.
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {int(len(month))}"])
    csvwriter.writerow([f"Total: ${(total)}"])
    csvwriter.writerow([f"Average Change: ${round(((pl_totalchange-first_pdchange)/(int(len(month))-1)),2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {date[maxpl_index]} (${(max(change_list))})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {date[minpl_index]} (${(min(change_list))})"])
