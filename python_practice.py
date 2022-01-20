#LISTS rectangle brackets
counties = ["Araphahoe", "Denver","Jefferson"]

print(counties)

#TUPLES are rounded brackets () and are immutable


#DICTIONARIES
counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438


print(counties_dict)

counties_dict.get("Denver")

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})


#inputs with print versus inputs with f strings

my_votes = int(input("How many votes did you get in the election? "))
total_votes =int(input("What is the total votes in the election? "))
print(f"I recieved {my_votes / total_votes * 100}% of the total votes. ")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:,2f}% of the total votes.")

print(message_to_candidate)
