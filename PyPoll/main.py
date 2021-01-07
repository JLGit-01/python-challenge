import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

voter = []
total_votes = 0
khan = 0



#read csv as text file
with open (election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip the header
    next(csvreader,None)

    for row in csvreader:
        voter.append(row[0])
        total_votes = total_votes + 1
    


print("Election Results")
print("--------------------")
print('Total Votes: ' + str(total_votes))


output_file = os.path.join('Analysis','election_data.csv')

   
with open(output_file, "w",newline="") as datafile:
    writer = csv.writer(datafile)


