twitter-analytics-parser
========================

A simple Python parser program for data from analytics.twitter.com

### Background ###
When I discovered https://analytics.twitter.com I was very exicted. Twitter + data = awesome! I was disappointed when I found out I couldn't sort columns by clicking on the column header, e.g. 'Impressions', 'Enagement Rate'. I was also disappointed when I couldn't find my Top Tweet of 2014. So I wrote this simple parser with Python to walk through the CSV file and calculate the top tweets based on RT's, Replies or Favorites.

### Requirements ###
- Python 2.7

### Setup ###
- Clone this repository
- Download CSV data from analytics.twitter.com via "Export Data" button
- Copy .csv file to home directory of this repository
- Make sure .csv is name 'twitter_activity_metrics.csv'

### Run Program ###
- Open a command window in the home directory of this repository (needs to have both twitter_activity_metrics.csv and twitter_metrics.py)
- Run `python twitter_metrics.py`

### Future Improvements ###
- Allow users to enter a value for `top_count` varaible. Currently it is set to 10 so lists will always be the "Top 10" tweets that meet the criteria
- Tie Breaking: If tweets are tied at the bottom of the list such that # 10 and # 11 have the same value either display the eleventh tweet or have some sort of tie breaking evaluation to select which should be on the list
- Allowing users to enter a date range 

### Contact ###
You can contact me about bugs, suggestions and general comments at emma at rocketdept.com
