import requests
from bs4 import BeautifulSoup

URLs = {
    'PPG': 'https://www.teamrankings.com/nfl/stat/points-per-game',
    'RTDPG': 'https://www.teamrankings.com/nfl/stat/rushing-touchdowns-per-game',
    'PassTD': 'https://www.teamrankings.com/nfl/stat/passing-touchdowns-per-game',
    'third_conv': 'https://www.teamrankings.com/nfl/stat/third-down-conversions-per-game',
    'turnover': 'https://www.teamrankings.com/nfl/stat/turnover-margin-per-game',
    'redZn': 'https://www.teamrankings.com/nfl/stat/red-zone-scoring-pct',
    'timeOfP' : 'https://www.teamrankings.com/nfl/stat/average-time-of-possession-net-of-ot'


}


team1 = input("Enter home team: ")
team2 = input("Enter away team: ")

team_stats = {} # initialize empty dicitonary

for key in URLs:
    team_stats[key] = {'team1': 0, 'team2': 0}    # give dictionary key-value pairs, where the key is the key of the
# URL dictionary (stat name) and the value is a dictionary containing the respective stat for each team (initialized to 0 here)


def scrape_data(url, key):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')  # parse data
    stat_html = soup.find('tbody')     # separate the groups of stats from the rest of the HTML

    stat_data = {}  # initialize empty dictionary for the stat data

    for row in stat_html.find_all('tr'):
        columns = row.find_all('td')
        team_name = columns[1].text.strip()  # extract team name from HTML
        team_stat = columns[2].text.strip()  # extract stat value from HTML

        if "%" in team_stat:    # if the stat is a percentage, remove the '%' sign so it can be converted to a float
            team_stat = float(team_stat.replace("%", ""))
        else:
            team_stat = float(team_stat)

        stat_data[team_name] = team_stat  # assigns the stat value to its respective team

    team_stats[key]['team1'] = stat_data.get(team1)  # assigns the corresponding stat name (key) as a key, and as its value assigns a subdictionary, with 'teamx' as the key and the stat value as its value
    team_stats[key]['team2'] = stat_data.get(team2)



def getWinner():
    team1_score = 0
    team2_score = 0
    for key, url in URLs.items():  # for each URL (or stat) in the dictionary, scrape its data
        scrape_data(url, key)

    for key in URLs:   # for each URL (stat)
        if team_stats[key]['team1'] > team_stats[key]['team2']:  # if team1 value > team2
            team1_score += 1 # give team 1 a point
        elif team_stats[key]['team2'] > team_stats[key]['team1']: # if team 2 value > team1
            team2_score +=1 # give team 2 a point

    if team1_score > team2_score:
        print(f"{team1} Wins This Matchup")
    elif team2_score > team1_score:
        print(f"{team2} Wins This Matchup")
    else:
        print("A matchup between these two teams is too close to call!")


getWinner()

