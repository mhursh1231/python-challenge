#Pull in data from budget_data.csv
import os
import csv

#Importing .csv file from local repo and outline of file path
script_dir = os.path.dirname(os.path.abspath('budget_data.csv'))

data_folder = os.path.join(script_dir, 'PyBank', 'Resources')

file_path = os.path.join(data_folder, 'budget_data.csv')

#Create the lists to store the data
profit = []
monthly_changes = []
date = []

#Initialize the variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
monthly_change_profits = 0

#Open the CSV file using the set path PyBankcsv
with open(file_path, 'r') as csvfile:
    #Create a CSV reader with dictionaries
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first
    csv_header = next(csvreader)

    #Iterate through the rows in the CSV files
    for row in csvreader:
        
        #Count number of months in dataset
        count = count + 1
        
        final_profit = int(row[1])
        
        #Average change in profits on monthly basis
        if count > 1:
            monthly_change_profits = final_profit - initial_profit
        
        #Need month count for calculations of greatest increase/decrease in profits
        date.append(row[0])

        #Add the profit information and calculate total profits
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        
        #Store monthly changes
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

    #Calculate the average change in profits
    average_change_profits = (total_change_profits)/(count - 1)
    formatted_average = format(average_change_profits, '.2f')
    print("Average Change Profits: {}".format(formatted_average))

    #Find the minimum and maximum in profits and respective dates 
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    date_increase = date[monthly_changes.index(greatest_increase_profits)]
    date_decrease = date[monthly_changes.index(greatest_decrease_profits)]

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(format(average_change_profits, '.2f')))
    print("Greatest Increase in Profits: " + str(date_increase) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("Average Change: " + "$" + str(format(average_change_profits, '.2f')) + "\n")
    text.write("Greatest Increase in Profits: " + str(date_increase) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(greatest_decrease_profits)+ ")\n")
    text.write("----------------------------------------------------------\n")