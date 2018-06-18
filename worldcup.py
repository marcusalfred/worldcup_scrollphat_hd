
import requests
import simplejson
import time
#import scrollphathd
#from scrollphathd.fonts import font5x5

# Display a progress bar for seconds
# Displays a dot if False
#DISPLAY_BAR = False

# Brightness of the seconds bar and text
#BRIGHTNESS = 0.3


while True:
    # Clear
    print("\033c")
    # Get Data for Current Game from worldcup.sfg.io
    r = requests.get('http://worldcup.sfg.io/matches/current.json')
    c = r.content
    j = simplejson.loads(c)

    # Once I introduce the scrollphathd I want to have match progress presented as dots below score.
    '''if DISPLAY_BAR:
        # Step through 15 pixels to draw the seconds bar
        for y in range(15):
            # For each pixel, we figure out its brightness by
            # seeing how much of "seconds_progress" is left to draw
            # If it's greater than 1 (full brightness) then we just display 1.
            current_pixel = min(seconds_progress, 1)

            # Multiply the pixel brightness (0.0 to 1.0) by our global brightness value
            scrollphathd.set_pixel(y + 1, 6, current_pixel * BRIGHTNESS)

            # Subtract 1 now we've drawn that pixel
            seconds_progress -= 1

            # If we reach or pass 0, there are no more pixels left to draw
            if seconds_progress <= 0:
                break
    else:
        # Just display a simple dot
        scrollphathd.set_pixel(int(seconds_progress), 6, BRIGHTNESS)'''

    for item in j:
        #timefrac = item['time'] / 90
        #game_progress = timefrac * 15
        # Home Team Country Code - Score | Away Team Score | Country Code
        print item['home_team']['code'], item['home_team']['goals'], " | ",item['away_team']['goals'], item['away_team']['code']
        # Current Match Time
        print item['time']
        # Trying to print only "goal" and "goal-penalty" from events - WIP
        '''if item['home_team_events'][0]["type_of_event"] == "goal":
            print item['home_team_events'][0]['player'], item['home_team_events'][0]['time']
        if item['away_team_events'][0]["type_of_event"] == "goal":
            print item['away_team_events'][0]['player'], item['away_team_events'][0]['time']'''


        #print timefrac
    # Every 50 Seconds
    time.sleep(50)
