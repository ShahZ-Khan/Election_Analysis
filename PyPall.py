# Add our dependencies
import csv
from email import header
import os
    # Assign a variable to load a file form a path
file_to_load = os.path.join("election_results.csv")
    # Assign a variable to load a file form a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
    #print(file_to_load)
    # 1. Initialize a total vote counter
total_vote = 0
Candidate_options =  []
#1 Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

    # Open the eletion results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add the total vote count.
        
        total_vote+=1
        #3 Print the total votes.
        
        # Print the candidate for each row.
        candidate_name =row[2]
        
        # Add the candidate name to the candidate list
        # If the candiddate does not match any existing candidate...
        if candidate_name not in Candidate_options:
        # Add it to the list of candidates.
            Candidate_options.append(candidate_name)
        #2.Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name]+=1
        # Determine the percentage of votes for each candidate by looping through the chart
        #1. Iterate through the candidate list
        for candidate_name in candidate_votes:
            

                
            #2. Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_vote) * 100
            # To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.

            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

             #if true than set winning_count = votes and winning_percent =
            #vote_percentage.
            winning_count = votes
             #And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
             #To do. print out each candidate's name, vote count, and percentage of
             #votes to the terminal.
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # To do. print out the winning candidate, vote count and percentage to 
            # terminal.
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
            print(winning_candidate_summary)
            




