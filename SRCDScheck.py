#!/usr/bin/env python3
#pip install pysrcds
from srcds.rcon import RconConnection
import re
#Variablen für Verbindung
#Checkname aren't allowed to spaces!!!
checkname = "CSS_Classic"
host = '192.168.254.194'
port = '27015'
rconpass = 'trololo'
#Connection
conn = RconConnection(host, port=port, password=rconpass)
response = conn.exec_command('status')
out = response.replace('\\n', '\n')
p = re.compile('players[^\n]*')
m = p.search(out)
#Group Text to have only one Line
serverstats=m.group()
players = re.findall(r'\d+', serverstats)
#Print line for CheckMK
print('P {} Spieler={};{};{};{};{} {} {} von {} Spieler auf dem Server'.format(checkname, str(players[0]), str(int(players[2])-2), str(players[2]), 0, str(players[2]), checkname, str(players[0]), str(players[2])))
