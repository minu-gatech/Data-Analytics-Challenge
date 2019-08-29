

''' PYTHON Homework 3 (Extra) -PyBoss '''


import os, csv
import re

filename = os.path.join("PyBoss_employee_data.csv")


''' Intiliazing Variables '''
EmpID = []
FirstName = []
LastName = []
dateofbirth_list = []
ssn_list = []
states = []


''' State Abbreviations Dictionary '''

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}		
		

''' Opening and Reading each record of csv file '''

with open (filename, 'r') as file:
	reader = csv.reader(file, delimiter = ',')
	header = next(reader)
	
	for row in reader:
	
		# Employee ID
		EmpID.append(row[0])
		
		# Splitting Name into First Name and Last Name
		fullname = row[1]
		name = fullname.split()
		FirstName.append(name[0])
		LastName.append(name[1])
		
		# Formatting DOB Column
		birth = row[2].split('-')
		dateofbirth = f"{birth[1]}/{birth[2]}/{birth[0]}"
		dateofbirth_list.append(dateofbirth)
		
		# SSN Formatting using regular expressions - search and replace function - sub()
		ssn = row[3].split('-')
		ssn[0] = re.sub("[0-9]","*",ssn[0])
		ssn[1] = re.sub("[0-9]","*",ssn[1])
		ssn = f"{ssn[0]}-{ssn[1]}-{ssn[2]}"
		ssn_list.append(ssn)
		
		# States re-written in two letter abbreviations
		state = row[4]
		for key in us_state_abbrev:
			if (state == key):
				state = us_state_abbrev[key]
				states.append(state)
		

''' Exporting the formatted output to CSV file '''

filename = "PyBoss_formatted_output.csv"
with open (filename,'w', newline='') as file:
	writer = csv.writer(file,delimiter=',')
	writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
	for i in range(len(EmpID)):
		writer.writerow([EmpID[i],FirstName[i],LastName[i],dateofbirth_list[i],ssn_list[i],states[i]])
		
		
		
	