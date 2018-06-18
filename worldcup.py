
import requests
import simplejson


r = requests.get('http://worldcup.sfg.io/matches/current.json')
c = r.content
j = simplejson.loads(c)

for item in j:
    print item['home_team']['code'], item['home_team']['goals'], " | ",item['away_team']['goals'], item['away_team']['code']
    print item['time']
