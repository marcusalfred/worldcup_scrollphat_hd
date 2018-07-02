

import requests #get World Cup Data
import json 	#used to parse World Cup JSON data
import time	  #returns time values
import datetime
import os
import unicodedata
import pytz
from pytz import timezone

import scrollphathd #default scrollphathd library
from scrollphathd.fonts import font3x5


world_cup = 1
POLL_INTERVAL = 15
DEBUG = 1
# Display settings
BRIGHT = 0.2
DIM = 0.1
fmt1 = '%Y-%m-%dT%H:%M:%SZ'
fmt2 = '%H:%M'
local_tz = timezone('US/Central')


# Brightness of the seconds bar and text
# BRIGHTNESS = 0.3


def mainloop():

    scrollphathd.clear()
    scrollphathd.show()

    print("\033c")
    current = 'http://worldcup.sfg.io/matches/current'
    today = 'http://worldcup.sfg.io/matches/today'

    today_games = requests.get(today)
    wc = today_games.json()

    #home_team1 = wc[0]['home_team']['code']
    #away_team1 = wc[0]['away_team']['code']
    #home_goals1 = wc[0]['home_team']['goals']
    #away_goals1 = wc[0]['away_team']['goals']
    #match_time1 = wc[0]['time']
    #match_date1 = wc[0]['datetime']
    #game_score = home_team1, home_goals1, " | ", away_goals1, away_team1

    for i in range(len(wc)):
        home_team = wc[i]['home_team']['code']
        away_team = wc[i]['away_team']['code']
        home_goals = wc[i]['home_team']['goals']
        away_goals = wc[i]['away_team']['goals']
        match_time = wc[i]['time']
        match_date = wc[i]['datetime']
        #dtt = match_date.strftime("%H:%M")
        dt = datetime.datetime.strptime(match_date, fmt1).replace(tzinfo=pytz.utc).astimezone(local_tz)
        dtf = dt.strftime(fmt2)

        if wc[i]['status'] == "in progress":
            print(wc[i]['home_team']['code'], wc[i]['home_team']['goals'],
            "|", wc[i]['away_team']['goals'], wc[i]['away_team']['code'], wc[i]['time'])
            scrollphathd.clear()
            scrollphathd.write_string("{0} {1} | {2} {3} {4}".format(home_team, home_goals, away_goals, away_team, match_time), x=0, y=1,font=font3x5, brightness=BRIGHT)
            time.sleep(1)

            while wc[i]['status'] == "in progress":
                scrollphathd.show()
                scrollphathd.scroll()
                time.sleep(.15)

            scrollphat.clear()
            scrollphathd.show()
            time.sleep(1)


        elif wc[i]['status'] == "future":
            future_game = (wc[i]['home_team']['code'], "|", wc[i]['away_team']['code'], wc[i]['datetime'])
            #future_game = "This Works"
            print(wc[i]['home_team']['code'], "|", wc[i]['away_team']['code'], wc[i]['datetime'])
            print(len(wc))
            scrollphathd.clear()
            scrollphathd.write_string("{0} | {1} {2} ".format(home_team, away_team, dtf), x=0, y=1,font=font3x5, brightness=0.4)
            time.sleep(1)

            while wc[i]['status'] == "future":
                scrollphathd.show()
                scrollphathd.scroll()
                time.sleep(.15)

            scrollphat.clear()
            scrollphathd.show()
            time.sleep(1)


        time.sleep(POLL_INTERVAL)

try:
    mainloop()

except KeyboardInterrupt:
    print("Exiting!")
