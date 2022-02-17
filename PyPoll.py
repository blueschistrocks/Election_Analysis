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

# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")


# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    
    #To do: read and analyze data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
   
    
   #for row in file_reader:
   #    print(row[0])