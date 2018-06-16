import os
import csv

# locate CSV files
dataA = os.path.join('.', 'Resources', 'budget_data_1.csv')
dataB = os.path.join('.', 'Resources', 'budget_data_2.csv')

# Open and read CSVs
with open(dataA, 'r', newline='') as csvfile:
    document = csv.reader(csvfile, delimiter=',')
    next(document)

    # Set Variables
    total_months= 0
    revenue_total= 0
    change = 0
    average = 0
    increase = 0
    decrease = 0

    # Create counters
    monthly_revenues = []
    monthly_changes = []
    nummonths = []

    # for loops
    for row in document:
        total_months=total_months+1
        revenue_total=revenue_total+int(row[1])
        monthly_revenues.append(int(row[1]))
        nummonths.append(str(row[0]))

    
    for i in range(1, len(monthly_revenues)):
        change = monthly_revenues[i]-monthly_revenues[i-1]
        monthly_changes.append(change)

    # Calculations
    average = sum(monthly_changes)/len(monthly_changes)
    increase = max(monthly_changes)
    decrease = min(monthly_changes)
    incr_month = nummonths[monthly_changes.index(increase)+1]
    decr_month = nummonths[monthly_changes.index(decrease)+1]

    # Print results
    print("Financial Analysis")
    print("-"*20)
    print("Total Months: "+str(total_months))
    print("Total Revenue: $"+str(revenue_total))
    print("Average Revenue Change: $"+str(average))
    print("Greatest Increase in Revenue: "+str(incr_month)+" $"+str(increase))
    print("Greatest Decrease in Revenue: "+str(decr_month)+" $"+str(decrease))
    print("-"*20)
      

    # Create new text file
output1 = os.path.join('output', 'results1.txt')
with open(output1, "w") as text_file:
    text_file.writelines('Financial Analysis\n')
    text_file.writelines('-------------------------\n')
    text_file.writelines('Total Months: ' + str(total_months) + '\n')
    text_file.writelines('Total Revenue: ' + '$'+str(revenue_total) + '\n')
    text_file.writelines('Average Revenue Change: ' + '$'+str(average) + '\n')
    text_file.writelines('Greatest Increase in Revenue ' + str(incr_month) + ' $'+str(increase) + '\n')
    text_file.writelines('Greatest Decrease in Revenue ' + str(decr_month) + ' $'+str(decrease) + '\n')
