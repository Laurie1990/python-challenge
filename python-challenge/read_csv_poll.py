## PyPoll

#Pages referenced in this homework assignment:
#https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python - creating a set of unique values from a list
#https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file#:~:text=Use%20csv%20module%20from%20Python's,pair%20in%20comma%20separated%20form.&text=The%20csv%20module%20contains%20DictWriter,list%20object%20containing%20field%20names.
#Above site page was use for reference when writing a dictionary to a CSV file using DictWriter

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

from collections import Counter

# Path to collect data from the Resources folder
csvpath = os.path.join('..', '03-Python','PyPoll', 'Resources', 'election_data.csv')


total_votes=0
Total=0
unique_count=0
data=0
candidate_list=[]
Per_cent_vote=0
poll_results=[]
csv_columns=['Candidate', 'Total votes', 'Per cent of vote']

#--------------------------------------------------------------------------------
#Count number of votes cast
with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
  print(csvreader)
    
  header=next(csvreader)
    
  for row in csvreader:
    total_votes += int(1)


print(f"Total votes cast: {total_votes}") 
#--------------------------------------------------------------------------------
#Create a list of candidates in poll by looping through last column, then passing list into a set to extract list of unique candidates
with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
    
  header=next(csvreader)
    
  for row in csvreader:
    # Add Candidate's name to a list
    candidate_list.append(row[2])

candidate_set=set(candidate_list)

candidate_list_2=list(candidate_set)

#print(candidate_list_2)

candidate_count=len(candidate_list_2)
print("There are", candidate_count, "candidates, with the following results:")


#--------------------------------------------------------------------------------
#Create a loop to go through unique list of candiates as specified in candidate_list_2, 
# and then for each candidate, go through and count the rows where the candidate voted for matches the unique name in candidate_list_2
#
for i in range(0,4):
  with open(csvpath, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",") 
    header=next(csvreader)

    data=[row[2] for row in csvreader if row[2]== candidate_list_2[i]]
    Total=len(data)
    Per_cent_vote= round(float((Total/total_votes)*100), 4)
#for each loop of the candidate, create a dictionary with candidate's name and results, and then 
    print(candidate_list_2[i], Total, str(Per_cent_vote)+'%')
    candict={
      "Candidate": candidate_list_2[i],
      "Total votes": Total,
      "Per cent of vote": str(Per_cent_vote)
    }
#Add each candidate dictionary to list of dictionaries
    poll_results.append(candict)
#Search list of dictionaries for candidate dictionary with highest number of votes, and identify a winner
Poll_Winner = max(poll_results, key=lambda x:x["Total votes"])

print(f'The winner of this election is {Poll_Winner["Candidate"]} with {Poll_Winner["Total votes"]} votes')


#--------------------------------------------------------------------------------
#Write Election results to a CSV file

# Specify the file to write to
output_path = os.path.join("..", "python-challenge", "PyPoll_Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.DictWriter(csvfile, fieldnames=csv_columns)

    # Write the results, by writing list of dictionaries poll_results[]
    csvwriter.writeheader()
    for data in poll_results:
      csvwriter.writerow(data)





