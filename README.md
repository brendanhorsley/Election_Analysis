# Election_Analysis

## Project Overview
The purpose of this project was to analyze results from a recent election held in Colorado.
The data included votes cast from 3 different counties and for 3 different candidates.
The project wanted to see based on the votes which county brought in the most number of votes and what percentage of total votes they accounted for.
Similarly, the project wanted to find which candidate won the election by popular vote and the percentage of votes they recieved.

## Resources
First, our python script wanted to find the results for the final vote count each county recieved, and the percentage of the vote that accounted for.
Utilizing a dictionary to keep track of all votes cast we ran a for statement to calculate the desired statistics.
![image](https://user-images.githubusercontent.com/96553988/150722772-3cbed203-89bb-4ba3-be31-d91b893450ef.png)
Once we found the final vote count and final vote percentage for each county the script utilized an if statement to find which county won the most votes.
![image](https://user-images.githubusercontent.com/96553988/150722868-ca411a86-7010-4778-bbaa-b0890de7e25f.png)
The results were then saved into a text file.
Similar script was run on the candidate names to find the total votes and percentages each candidate recieved.
Then analysis was conducted to find the candidate who won the popular vote and this data was also saved to our text file.
The script for winning candidate results can be found below.
![image](https://user-images.githubusercontent.com/96553988/150723004-754bc64b-2e0f-44c6-aee5-2b3dce15576a.png)

## Summary
The results from our analysis foudn that Denver was the largest county in terms of vote count and vote percentage.
Denver accoutned for 82.8% of the total votes cast, equalling 306,055 votes.
The winner of the election based on the popular vote was Diana DeGette recieving 272,892 total votes, accounting for 73.8% of all votes.
![image](https://user-images.githubusercontent.com/96553988/150723129-0f709ae0-db95-4ed8-b776-d65fb0decdfd.png)
The results can all be found in the election_results text file.

## Challenge Overview
The python script created for this election can be utilized for election beyond just this specific one.
The code was written in a way to read each candidate name and election distrct from the excel csv file instead of through manual input.
This means a completely different election with different candidates and locations can utilize this same script.
For example, if the print files were rewritten from "largest county" to "largest state", and "county votes" to "state votes", and so on, this script could be run on data from a federal election and would be able to calculate correct data accordingly.

