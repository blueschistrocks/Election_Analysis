# Election_Analysis
##Overview of Project

Tom and Seth (Client) have requested further analysis of the congressional election results for Arapahoe, Denver, Jefferson counties.  The original election analysis was conducted to determine the total votes for all three counties, total votes for each candidate, percentage of votes for each candidate and the winner of the election.  The client is interested in what the voter turnout for each county, the percentage of votes per county and which county had the highest voter turnout.


## Modification of the Original Python Code

The original python code was modified by adding the following code:

### Added to the code prior to the for loop.
#County Options list
county_options = []
#Empty dictionary for county votes
county_votes = {}

### Added to the code within the for loop.
# Add the county name to the county list.
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)

            #Begin tracking a county's votes count
            county_votes[county_name] = 0
        
        # Add a vote to that county's count.
        county_votes[county_name] += 1

The first section of the code established a county options list and a county votes dictionary prior to the for loop. The second section of the code was added within the for loop.  This section searched the data for county names and if not in the county options list added the county to the list.  Then the code tracked a county’s votes and added up each county’s vote.

## Analysis Results

- The total vote count for the congressional election was: 369,711.

- Below is a breakdown of the number and percentage of votes for the three counties in the precinct:
-- Jefferson: 10.5% (38,855)
-- Denver: 82.8% (306,055)
-- Arapahoe: 6.7% (24,801)

- The county with the largest vote count was: Denver at 82.8 percent of the vote.

- Below is a breakdown of the number and percentage of votes for each congressional candidate:
-- Charles Casper Stockham: 23.0% (85,213)
-- Diana DeGette: 73.8% (272,892)
-- Raymon Anthony Doane: 3.1% (11,606)

- The following indicates the winner of the congressional election and their vote count and percentage:

-- Winner: Diana DeGette
-- Winning Vote Count: 272,892
-- Winning Percentage: 73.8%

Click the following links for images of the terminal and text file output of the election analysis python script. Click this link to view the text file. 

## Proposal for Additional Election Analyses

The methods used in this election analysis can be modified to provide a further analysis of the congressional election and other elections.  I would like to propose the following:

1. Conducting a wider analysis of election data in the State of Colorado for other congressional district elections, gubernatorial elections, state senator elections, state representative elections and ballot initiative elections.  

2. An analysis of other state election date and federal election data. 

In addition to the analysis proposed above, a deeper analysis of the election data can be conducted using the Pandas Python package.

-- Analysis of the congressional election data to determine the number of votes and vote percentage each candidate received by county. 

-- With additional election data for Colorado an analysis of election historical trends in voter turnout by districts, counties and cities.  With the appropriate data this type of analysis could be conducted on a national scale as well.
