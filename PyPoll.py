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
import random 
import numpy
import datetime
import os

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
file_to_load = '/Users/cristy/Desktop/Data Analysis/election-analysis-MariaCalderon/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader= csv.reader(election_data)
    
    headers=next(file_reader)
    print(headers)
