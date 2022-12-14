import os
import csv

# Path to collect data from file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Path for output text file
reportpath = os.path.join('analysis', 'budget_resport.txt')

# Defined variables
totalmonths = 0
net_total = 0
average_change = 0
total = []
previous_total = 0
monthchange = []
total_change = []
greatest_in = ["",0]
greatest_dec = ["", 9999999]
total_change_list = []

# Open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
  
# Loop through to find total months
    for row in csvreader:
        # Count total months
        totalmonths += 1

        # Average change between months
        net_total += int(row[1])

        # Average change of total between months over the entire period
        average_change =(int(row[1]) - previous_total)
        previous_total = float(row [1])
        total_change_list = total_change_list + [average_change]
        monthchange = [monthchange] + [row[1]]

        # Greatest increase in profits (date + amount)
        if average_change>greatest_in[1]:
            greatest_in[1]= average_change
            greatest_in[0]= row[0]

        # Greatest decrease in profits (date + amount)
        if average_change<greatest_dec[1]:
            greatest_dec[1] = average_change
            greatest_dec[0] = row[0]
    average_change = sum(total_change_list)/len(total_change_list)


# Format for outputs
Output = (
    f"Financial Analysis \n"
    f"----------------------------\n"
    f"\n"
    f"Total Months: {totalmonths}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_in}\n"
    f"Greatest Decrease in Profits: {greatest_dec}\n"

) 
print(Output)

# save results to Resources folder
with open(reportpath, "w") as txtfile:
    txtfile.write(Output)



