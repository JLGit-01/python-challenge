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
average_profit = 0
previous = 0
#read csv as text file
with open (budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip the header
    next(csvreader,None)

    for row in csvreader:
        date.append(row[0])
        total_months = total_months + 1
        average_profit = average_profit + int(row[1])
        change = int(row[1]) - previous 
        average_change.append(change)
        previous = int(row[1])

        if change > greatest_profits[1]:
            greatest_profits[1] = change
            greatest_profits[0] = row[0]

        if change < least_profits[1]:
            least_profits[1] = change
            least_profits[0] = row[0]


    final_avg = sum(average_change[1:])/(len(average_change)-1)
    #print(total_months)
    print(len(date))
    print(average_profit)
   # print(average_change)
    print(round(final_avg,2))
    print(least_profits[0],least_profits[1])
    print(greatest_profits[0],greatest_profits[1])


    # when row =1
    # change  = 867884 - 0
    # average_change.append(867884)
    # previous = 867884
   
    # when r0w =2
    # chnage = 984655-867884 =11167
    # average_change.append(change)
    # previous = 984655



    # until row =86





    

    
    