#!/usr/bin/env python3
#pip install pysrcds
from srcds.rcon import RconConnection
import re
try:
    checkname = "HL2DM"
    host = '10.0.1.18'
    port = '27015'
    rconpass = 'changeme'

    conn = RconConnection(host, port=port, password=rconpass)
    response = conn.exec_command('status')
    out = response.replace('\\n', '\n')
    p = re.compile('players : [^\n]*')
    m = p.search(out)
    #Group Text to have only one Line
    serverstats=m.group()
    players = re.findall(r'\d+', serverstats)
    print('P {} Spieler={};{};{};{};{} {} {} von {} Spieler auf dem Server'.format(checkname, str(players[0]), str(int(players[2])-2), str(players[2]), 0, str(players[2]), checkname, str(players[0]), str(players[2])))
except Exception as e:
    print('2 {} - Server nicht erreichbar!'.format(checkname))

