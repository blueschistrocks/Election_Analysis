#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:28:08 2022

@author: robertvanderweele
"""

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate wom
# 5. The winner of the election based popular vote.


# Assign a variable for the file to load and the path.

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options list
candidate_options = []
#Candidate Options list
county_options = []
#Empty dictionary
candidate_votes = {}
#Empty dictionary3
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # Print the county name from each row.
        county_name = row[1]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begion tracking a candidate's votes count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        # Add the county name to the candidate list.
        if county_name not in county_options:
            # Add it to the list of candidates.
            county_options.append(county_name)

            #Begion tracking a county's votes count
            county_votes[county_name] = 0
        
        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        
    print(election_results, end="")
    #After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

      
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
           f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
        # 3. Print the total votes.
        #print(total_votes)
        #print(candidate_options)
        #print(candidate_votes)
        #print(county_votes)
    
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")  
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
    
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
             # If true then set winning_count = votes and winning_percent = vote_percentage.
             
             winning_count = votes
             winning_percentage = vote_percentage
             # And, set the winning_candidate equal to the candidate's name.
             winning_candidate = candidate_name
    
        #  To do: print out the winning candidate, vote count and percentage to
        #   terminal.
    
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)  
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    
    
    
    
    
    
    
    
    
    
    
    
    