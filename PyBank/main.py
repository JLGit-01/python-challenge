import os
import csv

budget_data_csv = os.path.join ('Resources', 'budget_data.csv')


#lists to store data

date = []
net_total_amount_profit_losses = []
average_change = []
greatest_profits = ["", 0]
least_profits = ["", 9999999]
total_months = 0
net_total = 0
previous = 0
#read csv as text file
with open (budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip the header
    next(csvreader,None)

    for row in csvreader:
        # Add date
        date.append(row[0])
        # Adds total months
        total_months = total_months + 1
        #Adds Grand total
        net_total = net_total + int(row[1])
        #Computes the change average by going row by row and holding those values to compute the average
        change = int(row[1]) - previous 
        average_change.append(change)
        previous = int(row[1])
        #Goes through and finds the greatest profit while performing the four loop
        if change > greatest_profits[1]:
            greatest_profits[1] = change
            greatest_profits[0] = row[0]
        #Goes through and find the least profit while performing the four loop
        if change < least_profits[1]:
            least_profits[1] = change
            least_profits[0] = row[0]

   # Grabs the final average utilizing the average change sum and length function for average change
    final_avg = sum(average_change[1:])/(len(average_change)-1)

   # Print out each of the parameters as requested
    print('Financial Analysis')
    print('----------------------')
    print(f"Total Months: {len(date)}")
    print('Total: $' + str(net_total))
    print(f"Average Change:  ${round(final_avg,2)}")
    print(f"Greatest Increase In Profits: {greatest_profits[0]} (${greatest_profits[1]})")
    print(f"Greatest Decrease In Profits: {least_profits[0]} (${least_profits[1]})")
    
output_file = os.path.join('Analysis','budget_data.csv')

   
with open(output_file, "w",newline="") as datafile:
    writer = csv.writer(datafile)




    

    
    