## PyBank
#----------------------------------------------------------------------------------------------------------------------
#Pages referenced in this homework assignment:
#https://stackoverflow.com/questions/35329573/finding-max-value-in-a-column-of-csv-file-python - for discussion on finding max values in a column
#https://python-forum.io/Thread-Count-of-unique-items-based-on-condition - for discussion on finding unique values in a column (somewhat redundant)
#https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python - for a discussion of summing a column






# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

from collections import Counter

# Path to collect data from the Resources folder
csvpath = os.path.join('..', '03-Python','PyBank', 'Resources', 'budget_data.csv')

row_count=0
Total=0
unique_count=0
data=0
poll_results={}
#--------------------------------------------------------------------------------
#Count number of rows (for use in average)
with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
    
  header=next(csvreader)
    
  for row in csvreader:
    row_count += int(1)


print(f"There are {row_count} months in the data") 

#--------------------------------------------------------------------------------
#Add up total of P/L column

with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
    
  header=next(csvreader)
    
  for row in csvreader:
    Total += float(row[1])

Average_Change= round(Total/row_count, 2)
print(f"The total value of P/L statements is ${Total}") 
print(f"Average  Change is ${Average_Change}") 

#--------------------------------------------------------------------------------
#Count number of UNIQUE rows (for count of months and years of P/L)
with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
    
  header=next(csvreader)
  
  data = [row[0] for row in csvreader] # List comprehension for simplicity
  unique_count = len(Counter(data)) # Pass the list to instantiate the Counter object


#Find Max change in P/L
with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
    
  header=next(csvreader)

  max_num = max(csvreader, key=lambda row: int(row[1]))

#Find Min change in P/L
with open(csvpath, "r") as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter = ",")
    
  header=next(csvreader)

  min_num = min(csvreader, key=lambda row: int(row[1]))

#print(f"There are {unique_count} UNIQUE ROWS") 
print("the month with the max change is", max_num[0], "with a change of $",max_num[1])
print("the month with the min change is", min_num[0], "with a change of $",min_num[1])


#-----------------------------------------------------------------------------------
#Write results to a csv file

# Specify the file to write to
output_path = os.path.join("..", "python-challenge", "PyBank_Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=":")

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    # Write the results
    csvwriter.writerow([f"Total Months: {row_count}"])
    csvwriter.writerow([f"Total: ${Total}"])
    csvwriter.writerow([f"Average  Change: ${Average_Change}"])
    csvwriter.writerow([f"reatest Increase in Profits: {max_num[0]}, ({max_num[1]})"])
    csvwriter.writerow([f"reatest Increase in Profits: {min_num[0]}, ({min_num[1]})"])



