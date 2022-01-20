import csv
import os

#Open the elections results as readable
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a new file to save our data to
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open file as text file using a with statement
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)

   #read and print the header row
   headers = next(file_reader)
   print(headers)




#close the file



#Data we need to retrieve.
#1. The total number of votes cast
#2.  A complete list of candidates
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

