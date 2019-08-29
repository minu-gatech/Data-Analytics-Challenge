
''' PYTHON Homework 3 - PyBank '''



''' Importing modules '''

import os, csv
filename = os.path.join("PyBank_Resources_budget_data.csv")

''' Intializing Variables '''

total_months = 0
net_profit_losses = 0
changes_list = []
difference_list = []
greatest_increase_profit = 0
greatest_decrease_losses = 0
profit_date = ''
losses_date = ''
average_changes = 0
number = 0

''' Opening and Reading a csv file '''

with open(filename,'r') as file:
	reader = csv.reader(file,delimiter=',')
	header = next(reader)
	#print(header)
	for row in reader:
		
		#The total number of months included in the dataset
		if row[0] != '':
			total_months = total_months + 1
			
		#The net total amount of "Profit/Losses" over the entire period	
		if row[1] != '':
			net_profit_losses = net_profit_losses + int(row[1])

		#The average of the changes in "Profit/Losses" over the entire period
		changes_list.append(int(row[1]))
	
		#The greatest increase in profits (date and amount) over the entire period
		if int(row[1]) > greatest_increase_profit:
			greatest_increase_profit = int(row[1])
			profit_date = row[0]
		
		#The greatest decrease in losses (date and amount) over the entire period
		if int(row[1]) < greatest_decrease_losses:
			greatest_decrease_losses = int(row[1])
			losses_date = row[0]
			
			
''' The average of the changes in "Profit/Losses" over the entire period '''
for i in range(len(changes_list)):
			difference_list.append(int(changes_list[i]) - number)
			number = int(changes_list[i])
			#print(difference_list)
total = 0			
for each in difference_list:			
	 total = each + total
	 
average_changes = total / len(difference_list)

	

	
''' Printing output to teminal		 '''
output1 = "\n FINANCIAL ANALYSIS"		
print(output1)	
print("-"*20)
print(f" Total Months : {total_months} \n Total : ${net_profit_losses} \n Average Change : ${average_changes} \n Greatest Increase in Profits: {profit_date} (${greatest_increase_profit}) \n Greatest Decrease in Profits: {losses_date} (${greatest_decrease_losses})")	


''' Exporting the output to text file	'''
file = open("PyBank_Analysis_Output.txt",'w')
file.write(output1 + "\n")
file.writelines("-"*20)
file.write(f"\n Total Months : {total_months} \n Total : ${net_profit_losses} \n Average Change : ${average_changes} \n Greatest Increase in Profits: {profit_date} (${greatest_increase_profit}) \n Greatest Decrease in Profits: {losses_date} (${greatest_decrease_losses})")	


