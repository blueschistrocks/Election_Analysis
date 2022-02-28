# Election_Analysis
## Overview of Project

Tom and Seth (Client) have requested further analysis of the congressional election results for Arapahoe, Denver, Jefferson counties.  The original election analysis was conducted to determine the total votes for all three counties, total votes for each candidate, percentage of votes for each candidate and the winner of the election.  The client is interested in the voter count for each county, the percentage of votes per county and which county had the highest voter count.

 - The original code is available for review at this [Link](https://github.com/blueschistrocks/Election_Analysis/blob/6795acfc5f725e06134841345478f3b283a24337/PyPoll.py)

 - The modified code is available for review at this [Link](https://github.com/blueschistrocks/Election_Analysis/blob/71ce2c34143d55ad94a9955ee6e45b24298f4c26/PyPoll_Challenge.py)

## Modification of the Original Python Code

The original python code was modified by adding the following code:

        ##Added to the code prior to the for loop.
        #County Options list
        county_options = []
        #Empty dictionary for county votes
        county_votes = {}
        #Track the largest county and county voter count.
        largest_county_vote = ""
        winning_county_count = 0
        winning_county_percentage = 0

### 
        ##Added to the code within the for loop.
        #Add the county name to the county list.
        if county_name not in county_options:
            #Add it to the list of counties.
            county_options.append(county_name)

            #Begin tracking a county's votes count
            county_votes[county_name] = 0
        
        #Add a vote to that county's count.
        county_votes[county_name] += 1
        
  ###
        ##Added to the code to retrive the county votes, calculate county percentage and the county information to the text file and terminal.
        #Write a for loop to get the counties from the county dictionary.
          for county_name in county_votes:

              # 6b and 6c: Retrieve the county vote count and calculate the percentage of votes for the county.
              c_votes = county_votes.get(county_name)
              c_vote_percentage = float(c_votes) / float(total_votes) * 100
              county_results = (
                  f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

              # 6d: Print the county results to the terminal.
              print(county_results)
              # 6e: Save the county votes to a text file.
              txt_file.write(county_results)

              # 6f: Write an if statement to determine the winning county and get its vote count.
              if (c_votes > winning_county_count) and (c_vote_percentage > winning_county_percentage):
                   winning_county_count = c_votes
                   winning_county = county_name
                   winning_county_percentage = c_vote_percentage
  ###
          ##Added to the code to add the largest county to the text file and terminal.
          #Print the county with the largest turnout to the terminal.
          winning_county_summary = (
              f"-------------------------\n"
              f"Largest County Turnout: {winning_county}\n"
              f"-------------------------\n")
          print(winning_county_summary)
          # 8: Save the county with the largest turnout to a text file.
          txt_file.write(winning_county_summary)


The first section of the code established a county options list and a county votes dictionary prior to the for loop. The second section of the code was added within the for loop.  This section searched the data for county names and if not in the county options list added the county to the list.  Then the code tracked a county’s votes and added up each county’s vote.  The third section of code calculated the percentage of votes for each county and the county with the most votes then added this information to the text file and terminal output. The forth section of code added the county with the most votes to the text file and terminal output.

## Analysis Results

#### The total vote count for the congressional election was: 369,711.

- Below is a breakdown of the number and percentage of votes for the three counties in the precinct:
   - Jefferson: 10.5% (38,855)
   - Denver: 82.8% (306,055)
   - Arapahoe: 6.7% (24,801)

#### The county with the largest vote count was: Denver at 82.8 percent of the vote.

- Below is a breakdown of the number and percentage of votes for each congressional candidate:
   - Charles Casper Stockham: 23.0% (85,213)
   - Diana DeGette: 73.8% (272,892)
   - Raymon Anthony Doane: 3.1% (11,606)

- The following indicates the winner of the congressional election and their vote count and percentage:
   - Winner: Diana DeGette
   - Winning Vote Count: 272,892
   - Winning Percentage: 73.8%

- Click the following links for images of the terminal and a copy of the text file output of the election analysis python script. 
  - Click this [Link](https://github.com/blueschistrocks/Election_Analysis/blob/d56125dd92909dd2e8c181096415e863222bbb3f/analysis/Terminal_output.png) to view the terminal output. 
  - Click this [Link](https://github.com/blueschistrocks/Election_Analysis/blob/7da71878493114e7312cc82fe919cdd4889e8ad8/analysis/election_analysis.txt) to view the text file. 

## Proposal for Additional Election Analyses

The methods used in this election analysis can be modified to provide a further analysis of the congressional election and other elections.  I would like to propose the following:

- Conducting a wider analysis of election data in the State of Colorado for other congressional district elections, gubernatorial elections, state senator elections, state representative elections and ballot initiative elections.  

- An analysis of other state election data and federal election data. 

In addition to the analysis proposed above, a deeper analysis of the election data can be conducted using the Pandas Python package.

- Analysis of the congressional election data to determine the number of votes and vote percentage each candidate received by county. 

- With additional election data for Colorado an analysis of election historical trends in voter turnout by districts, counties and cities.  With the appropriate data this type of analysis could be conducted on a national scale as well.
