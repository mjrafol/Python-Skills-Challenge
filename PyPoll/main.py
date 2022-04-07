# Module for code to run across multiple systems.
import os

# Module for reading a csv file.
import csv

# Set path for the input csv file.
csvpath = os.path.join('Resources','election_data.csv')

# Set list for votes and candidates.
ballot = []
candidates = []

# Set variables for candidate counters.
counter_c1 = 0
counter_c2 = 0
counter_c3 = 0

# Set dictionaries for the election results.
election_results = {}

# Open and read the csv file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store the header row.
    csvheader = next(csvreader)

    # Read through the records and calculate the analysis requirements.
    for row in csvreader:

        # Store ballot into a list.
        ballot.append(row[0])

        # Store candidate into a list.
        if row[2] not in candidates:
            candidates.append(row[2])
        
        # Set a counter for election votes to candidate 1.
        if row[2] == candidates[0]:
            counter_c1 = counter_c1 + 1

        # Set a counter for election votes to candidate 2.
        elif row[2] == candidates[1]:
            counter_c2 = counter_c2 + 1

        # Set a counter for election votes to candidate 3.
        elif row[2] == candidates[2]:
            counter_c3 = counter_c3 + 1


    # Dictionary that shows candidate name as key and total individual ballot count as value.
    election_results = {candidates[0] : counter_c1, 
                        candidates[1] : counter_c2,
                        candidates[2] : counter_c3}
    
# Print the analysis data requirements.
print("Election Results")
print("----------------------------")

# Total votes/ballot count.
print(f"Total Votes: {int(len(ballot))}")
print("----------------------------")

# Each candidate's total votes and percent of votes.
print(f"{candidates[0]} : {round((counter_c1/(int(len(ballot)))*100),3)}% ({counter_c1})")
print(f"{candidates[1]} : {round((counter_c2/(int(len(ballot)))*100),3)}% ({counter_c2})")
print(f"{candidates[2]} : {round((counter_c3/(int(len(ballot)))*100),3)}% ({counter_c3})")
print("----------------------------")

# Winner.
print(f"Winner: {max(election_results, key=election_results.get)}")
print("----------------------------")

# Create a list for the analysis result requirements to be printed in output text file.
output_lines = ["Election Results", 
    "----------------------------", 
    f"Total Votes: {int(len(ballot))}", 
    "----------------------------",
    f"{candidates[0]} : {round((counter_c1/(int(len(ballot)))*100),3)}% ({counter_c1})",
    f"{candidates[1]} : {round((counter_c2/(int(len(ballot)))*100),3)}% ({counter_c2})",
    f"{candidates[2]} : {round((counter_c3/(int(len(ballot)))*100),3)}% ({counter_c3})",
    "----------------------------",
    f"Winner: {max(election_results, key=election_results.get)}",
    "----------------------------"]

# Export a text file with the analysis results in designated path.
with open (os.path.join('Analysis','PyPoll_output.txt'),'w') as txtoutput:

    # Write the analysis results.
    for line in output_lines:
        txtoutput.write(line)
        txtoutput.write('\n')
