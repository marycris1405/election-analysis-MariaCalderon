#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:09:03 2019

@author: cristy
"""

#The data we need to retrieve.
# 1. The Total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

import csv
import os
import random 
import numpy
import datetime

dir(csv)
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)
    
##Code

# Assign a variable to load a file from a path.
file_to_load = '/Users/cristy/Desktop/Data_Analysis/election-analysis-MariaCalderon/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Initialize a total vote counter 
total_votes=0

#Candidates Options
candidate_options=[]

#Candidates votes
candidates_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate= " "
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader= csv.reader(election_data)
    
    #Read the header row
    headers=next(file_reader)
    #print(headers)
    
    #Print each row int he CSV file
    for row in file_reader:
        
        #Add to the total vote count
        total_votes+=1
        
        #Print the candidate name from each row
        candidate_name= row[2]
        
        #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)      
            
            #Begin tracking that candidate's vote count
            candidates_votes[candidate_name]=0
            
        #Add a vote to the candidate's count
        candidates_votes[candidate_name]+=1

        #print(total_votes)
        #print (candidate_options)
        #print (candidates_votes)
        
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidates_votes:
    # Retrieve vote count of a candidate.
    votes = candidates_votes[candidate]
    
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print the candidate name and percentage of votes.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
    #To do: print out each candidate's name, vote count, and percentage of
    #votes to the terminal.
    
    #Determine winning vote count and candidate
    #Determine if the vote is greater than the winning count.
   
    if (votes> winning_count) and (vote_percentage> winning_percentage):
        #If true the set winning_count=votes and winning_percentage=
        #vote percentage
        winning_count=votes
        
        winning_percentage=vote_percentage
        
        #And, set the winning_candidate equal to the candidate's name 
        winning_candidate=candidate
        
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
        


    
