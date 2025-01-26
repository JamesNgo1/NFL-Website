import requests
from bs4 import BeautifulSoup as soup
import csv 
from utils import scrape_url

# URLs for the stats for each stat category
passing_qb_page = requests.get('https://www.nfl.com/stats/player-stats/')
rushing_page = requests.get('https://www.nfl.com/stats/player-stats/category/rushing/2024/post/all/rushingyards/desc')
receiving_page = requests.get('https://www.nfl.com/stats/player-stats/category/receiving/2024/post/all/receivingreceptions/desc')

# headers from NFL stats sites for each stat category
passing_yards_headers = ["Player Name", "Passing Yards", " Yards/Attempt", "Attempt","Completions","Completions Percentage","Touchdowns","Interceptions","Rating","1st","1st%","20+", "40+", "Lng" , "sack", "sack yards"]
rushing_yards_headers = ["Player Name", "Rushing Yards", "attempts", "Touchdowns", "20 plus yards", "40 plus yards", "Long", "rushing 1st down", "Rushing 1st % " , "Fumbles"]
receiving_yards_headers = ["Player Name","Receptions", "Receiving Yards","Touchdowns", "20 plus yards", "40 plus yards", "Long", "1st down receptions", "1st % " , "fumbles " ," yac yards ber recpetions " , "targets"]


passing_csv = "passingYards.csv"
receiving_csv = "receivingYards.csv"
rushing_csv = "rushingYards.csv"


scrape_url(rushing_page,rushing_yards_headers,rushing_csv)






