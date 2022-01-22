import csv
import os

#Open the elections results as readable
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a new file to save our data to
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

#creating a list of candidate names
candidate_options = []
#creating a dictionary of votes for candidates
candidate_votes = {}

#Add a winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open file as text file using a with statement
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)

   #read and print the header row
   headers = next(file_reader)

  #Determine total votes in election and total votes for each candidate 
   for row in file_reader:
      total_votes += 1
      candidate_name = row[2]

      if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)

         candidate_votes[candidate_name] = 0

      candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
   election_results = (
      f"\nElection Results\n"
      f"----------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"----------------------\n")

   print(election_results, end="")

   txt_file.write(election_results)

#Determine vote percentage for each candidate
   for candidate_name in candidate_votes:
      votes = candidate_votes[candidate_name]
      vote_percentage = float(votes) /float(total_votes) * 100

      #Determine winning vote count and candidate 
      if (votes > winning_count) and (vote_percentage > winning_percentage):

         winning_count = votes
         winning_percentage = vote_percentage
         winning_candidate = candidate_name

   winning_candidate_summary = (
      f"----------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"----------------------\n")

   print(winning_candidate_summary)

   txt_file.write(winning_candidate_summary)


#close the file



#Data we need to retrieve.
#1. The total number of votes cast
#2.  A complete list of candidates
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

