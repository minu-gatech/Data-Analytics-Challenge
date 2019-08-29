
''' PYTHON Homework 3 - PyPoll '''


'''Importing modules'''

import os, csv

filename = os.path.join("PyPoll_Resources_election_data.csv")

''' Intializing Variables'''
total_votes_cast = 0
candidates_list = []
candidate = ''
total_votes = []
khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0

votes_count = {}

''' Opening and Reading a csv file '''

with open(filename,'r') as file:
	reader = csv.reader(file,delimiter=',')
	header = next(reader)
	#print(header)
	for row in reader:
		
		# The total number of votes cast
		if row[0] != '':
			total_votes_cast = total_votes_cast + 1
			
		# Complete list of candidates who received votes
		candidate = row[2]
		if(candidate not in candidates_list):
			candidates_list.append(candidate)
		
		
		# The total number of votes each candidate won
		if row[2] == 'Khan':
			khan_count = khan_count + 1
		elif row[2] == 'Correy':
			correy_count = correy_count + 1
		elif row[2] == 'Li':
			li_count = li_count + 1
		elif row[2] == "O'Tooley":
			tooley_count = tooley_count + 1
		else:
			print("\n\nNO CANDIDATES")
			
		
		# The percentage of votes each candidate won
		khan_won_percent = (khan_count / total_votes_cast) * 100
		correy_won_percent = (correy_count / total_votes_cast) * 100
		li_won_percent = (li_count / total_votes_cast) * 100
		tooley_won_percent = (tooley_count / total_votes_cast) * 100
		
		
		#The winner of the election based on popular vote.
		if(khan_count > correy_count and khan_count > li_count and khan_count > tooley_count):
			winner = 'Khan'
		if(correy_count > khan_count and correy_count > li_count and correy_count > tooley_count):
			winner = 'Correy'
		if(li_count > khan_count and li_count > correy_count and li_count > tooley_count):
			winner = 'Li'
		if(tooley_count > correy_count and tooley_count > khan_count and tooley_count > li_count):
			winner = "O'Tooley"	
			
			
		
''' Printing output to teminal	'''
output1 = "\n ELECTION RESULTS"		
print(output1)	
print("-"*30)
print(f" Total Votes : {total_votes_cast}")
print("-"*30)
print(f" {candidates_list[0]}: {khan_won_percent:.3g}.000% ({khan_count})")
print(f" {candidates_list[1]}: {correy_won_percent:.3g}.000% ({correy_count})")
print(f" {candidates_list[2]}: {li_won_percent:.3g}.000% ({li_count})")
print(f" {candidates_list[3]}: {tooley_won_percent:.3g}.000% ({tooley_count})")
print("-"*30)
print(f" Winner : {winner}")
print("-"*30)




''' Exporting the output to text file '''
file = open("PyPoll_Analysis_Output.txt",'w')
file.write(output1 + "\n")
file.writelines("-"*30)
file.write(f"\n Total Votes : {total_votes_cast}\n")
file.write("-"*30)
file.write(f"\n {candidates_list[0]}: {khan_won_percent:.3g}.000% ({khan_count})\n")
file.write(f" {candidates_list[1]}: {correy_won_percent:.3g}.000% ({correy_count})\n")
file.write(f" {candidates_list[2]}: {li_won_percent:.3g}.000% ({li_count})\n")
file.write(f" {candidates_list[3]}: {tooley_won_percent:.3g}.000% ({tooley_count})\n")
file.writelines("-"*30)
file.write(f"\n Winner : {winner}\n")
file.write("-"*30)



