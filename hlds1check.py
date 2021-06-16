#!/usr/bin/env python3
#pip install rHLDS
from rHLDS import Console
import re
checkname = "Ricochet"
host = '192.168.254.194'
port = '27015'
rconpass = 'trololo'

# Default port 27015
srv = Console(host=host, port=port, password=rconpass)

# Connect to server
srv.connect()

#Execute Status command and save result in variable
out = srv.execute("status")
p = re.compile('players[^\n]*')
m = p.search(out)
#Group Text to have only one Line
serverstats=m.group()
#Regex to extract only the numbers
players = re.findall(r'\d+', serverstats)
#Print line to parse it for CheckMK
print('P {} Spieler= {};{};{};{};{} {} {} von {} Spieler auf dem Server'.format(checkname, str(players[0]), str(int(players[1])-2), str(players[1]), 0, str(players[1]), checkname, str(players[0]), str(players[1])))
# Сlose connection
srv.disconnect()
