# NFL_scraper.py
## Overview

This Python script compares NFL team statistics from various categories, helping you determine which team might win in a head-to-head matchup based on the provided statistics. The script retrieves data from TeamRankings.com for specified categories and compares the statistics for two teams entered by the user.

## Features

- **Stat Categories:** The script currently compares teams in the following categories:
  - Points Per Game (PPG)
  - Rushing Touchdowns Per Game (RTDPG)
  - Passing Touchdowns Per Game (PassTD)
  - Third Down Conversions Per Game (third_conv)
  - Turnover Margin Per Game (turnover)
  - Red Zone Scoring Percentage (redZn)
  - Time of Possession (timeOfP)
 

- **User Input:** Users must input the names of two teams they want to compare.
  
- ##TEAM NAMES**
  - You MUST use the team's city as their name (i.e Kansas City for the Chiefs), except for the following teams:
    - LA Rams
    - LA Chargers
    - NY Jets
    - NY Giants

- **Winner Determination:** The score is calculated a score based on which team has a higher statistic in each category. The team with the higher score is declared the winner.

**Running the Script** 
- execute the code by running the sxript
- follow the prompts that appear and input the team names, making sure to follow naming the rules above
  
## Example

Enter home team: New England 
Enter away team: Kansas City 

Kansas City Wins This Matchup!

**Acknowledgments**
-Data sourced from TeamRankings.com
