#!/usr/bin/env python

import signal
import time
import requests
import simplejson

import scrollphathd

print("""
Scroll pHAT HD: Hello World

Scrolls "Hello World" across the screen
using the default 5x7 pixel large font.

Press Ctrl+C to exit!

""")

r = requests.get('http://worldcup.sfg.io/matches/current.json')
c = r.content
j = simplejson.loads(c)
score = item['home_team']['code'], item['home_team']['goals'], " | ",item['away_team']['goals'], item['away_team']['code']

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
#scrollphathd.rotate(degrees=180)

# Write the "Hello World!" string in the buffer and
#   set a more eye-friendly default brightness
scrollphathd.write_string(score, brightness=0.5)

# Auto scroll using a while + time mechanism (no thread)
while True:
    # Get Data for Current Game from worldcup.sfg.io
    r = requests.get('http://worldcup.sfg.io/matches/current.json')
    c = r.content
    j = simplejson.loads(c)
    score = item['home_team']['code'], item['home_team']['goals'], " | ",item['away_team']['goals'], item['away_team']['code']

    for item in j:
        #timefrac = item['time'] / 90
        #game_progress = timefrac * 15
        # Home Team Country Code - Score | Away Team Score | Country Code
        print item['home_team']['code'], item['home_team']['goals'], " | ",item['away_team']['goals'], item['away_team']['code']
        # Current Match Time
        print item['time']

    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
