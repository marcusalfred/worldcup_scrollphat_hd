import requests #get World Cup Data
import json 	#used to parse World Cup JSON data
import time	  #returns time values
import datetime
import os
import pytz
from pytz import timezone
#import logging

import scrollphathd #default scrollphathd library
from scrollphathd.fonts import font3x5




# Display settings
BRIGHT = 0.35
DIM = 0.1

# Time
fmt1 = '%Y-%m-%dT%H:%M:%SZ'
fmt2 = '%H:%M'
local_tz = timezone('US/Central')


while True:

    #logging.basicConfig(filename='worldcup.log', level=logging.DEBUG)
    #logging.debug('Started')

    #scrollphathd.clear()
    #scrollphathd.show()

    #print("\033c")

    #Software For Good World Cup API
    current = 'http://worldcup.sfg.io/matches/current'
    today = 'http://worldcup.sfg.io/matches/today'

    # GET Today's Games
    today_games = requests.get(today)
    # JSON Response Content for Today's Games
    wc = today_games.json()

    # Switch wc & wc1 to test with different game statuses
    with open('today.json') as json_file:
        wc1 = json.load(json_file)



    for i in wc:

        # Define Variables for scrollphathd
        home_team = i['home_team']['code']
        away_team = i['away_team']['code']
        home_goals = i['home_team']['goals']
        away_goals = i['away_team']['goals']
        match_time = i['time']
        match_date = i['datetime']
        sts = i['status']

        # Convert match_date from UTC to CST and format in 24 Hour time
        dt = datetime.datetime.strptime(match_date, fmt1).replace(tzinfo=pytz.utc).astimezone(local_tz)
        dtf = dt.strftime(fmt2)


        # if game status 'sts' is "in progress" print Team Codes/Scores/Elapsed Time ... WIP(scrollphat write string)
        if sts == "in progress":
                print(i['home_team']['code'], i['home_team']['goals'],
                "|", i['away_team']['goals'], i['away_team']['code'], i['time'])
                #scrollphathd.clear()
                #scrollphathd.write_string("{0} {1} | {2} {3} {4} < > ".format(home_team, home_goals, away_goals, away_team, match_time), x=0, y=1,font=font3x5, brightness=BRIGHT)

                #while sts == "in progress":
                #   scrollphathd.show()
                #   scrollphathd.scroll_to(x=str_len, y=0)
                #   time.sleep(.1)

                #scrollphat.clear()
                #scrollphathd.show()
                time.sleep(.5)

        #if game status 'sts' is "future" print Team Codes/Match Time ... WIP(scrollphat write string)
        elif sts == "future":
                print(i['home_team']['code'], "|",
                 i['away_team']['code'], dtf)
                #print(len(wc))
                #scrollphathd.clear()
                #scrollphathd.write_string("{0} | {1} {2} < > ".format(home_team, away_team, dtf), x=0, y=1,font=font3x5, brightness=BRIGHT)

                #while sts == "future":
                #    scrollphathd.show()
                #    scrollphathd.scroll()
                #    time.sleep(.1)

                #scrollphat.clear()
                #scrollphathd.show()
                time.sleep(.5)

        #if game status 'sts' is "completed" print Team Codes/Score/Winner ... WIP(scrollphat write string)
        elif sts == "completed":
                print(i['home_team']['code'], i['home_team']['goals'],
                "|", i['away_team']['goals'], i['away_team']['code'])
                #scrollphathd.clear()
                #scrollphathd.write_string("{0} {1} | {2} {3} < > ".format(home_team, home_goals, away_goals, away_team), x=0, y=1,font=font3x5, brightness=BRIGHT)

                #while sts == "completed":
                #    scrollphathd.show()
                #    scrollphathd.scroll()
                #    time.sleep(.1)

                #scrollphat.clear()
                #scrollphathd.show()
                time.sleep(.5)

        time.sleep(10)
