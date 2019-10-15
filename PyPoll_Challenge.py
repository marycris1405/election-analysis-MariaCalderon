#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:27:32 2019

@author: cristy
"""

import csv
import os
    
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

#County Options
county_options=[]

#County votes
county_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate= " "
winning_count=0
winning_percentage=0

#Winning County and Winning Count Tracker
winning_county= " "
winningc_count=0
winningc_percentage=0

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
        
        #Print the county name for each row
        county_name=row[1]
        
        #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)      
            
            #Begin tracking that candidate's vote count
            candidates_votes[candidate_name]=0
            
        #Add a vote to the candidate's count
        candidates_votes[candidate_name]+=1
        
        #Add the county name to the county list
        if county_name not in county_options:
            # Add it to the list of county.
            county_options.append(county_name)      
            
            #Begin tracking that county's vote count
            county_votes[county_name]=0
            
        #Add a vote to the county's count
        county_votes[county_name]+=1
        
        #Save the results to our text file
with open (file_to_save, "w")as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes: \n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    
    
        #print(total_votes)
        #print (candidate_options)
        #print (candidates_votes)

###############################################################################
# County Votes
###############################################################################        

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for county in county_votes:
        # Retrieve vote count of a candidate.
        votes_county = county_votes[county]
        
        # Calculate the percentage of votes.
        votec_percentage = float(votes_county) / float(total_votes) * 100
        
        #  Save the candidate results to our text file.
        # Print the candidate name and percentage of votes.
        county_results=(f"{county}: {votec_percentage:.1f}% ({votes_county:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        
        #Determine winning vote count and candidate
        #Determine if the vote is greater than the winning count.
       
        if (votes_county> winningc_count) and (votec_percentage> winningc_percentage):
            #If true the set winning_count=votes and winning_percentage=
            #vote percentage
            winningc_count=votes_county
            
            winningc_percentage=votec_percentage
            
            #And, set the winning_candidate equal to the candidate's name 
            winning_county=county
            
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    #Save winning candidate's results to the text file.
    txt_file.write(winning_county_summary)

###############################################################################        
# Candidates Votes
###############################################################################        

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidates_votes:
        # Retrieve vote count of a candidate.
        votes = candidates_votes[candidate]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #  Save the candidate results to our text file.
        # Print the candidate name and percentage of votes.
        candidates_results=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
                
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidates_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidates_results)
                
        #Determine winning vote count and candidate
        #Determine if the vote is greater than the winning count.
       
        if (votes> winning_count) and (vote_percentage> winning_percentage):
            #If true the set winning_count=votes and winning_percentage=
            #vote percentage
            winning_count=votes
            
            winning_percentage=vote_percentage
            
            #And, set the winning_candidate equal to the candidate's name 
            winning_candidate=candidate

###############################################################################        
# Winning Candidate
###############################################################################               

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

        
