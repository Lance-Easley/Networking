import socket
from _thread import *
import sys
from player import Player, Absent
import pickle

server = "192.168.1.141"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(9)
print("[GAME] Waiting for a connection, Server Started")

player_list = [
    Player(0, 0, 40, 60, (255, 0, 0)), Player(100, 0, 40, 60, (0, 0, 255)), Player(200, 0, 40, 60, (0, 255, 0)), 
    Player(0, 100, 40, 60, (255, 128, 0)), Player(100, 100, 40, 60, (128, 0, 255)), Player(200, 100, 40, 60, (0, 128, 0)), 
    Player(0, 200, 40, 60, (255, 255, 0)), Player(100, 200, 40, 60, (255, 0, 255)), Player(200, 200, 40, 60, (0, 255, 255)), 
    ]

player = 0
connected = set()
players = {}

def threaded_client(conn, playerId):
    global player
    conn.send(pickle.dumps(players[playerId]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) # Truanced: increase number

            if playerId in players:
                p = players[playerId]
            
                players[playerId] = data

                if not data:
                    print("[ERROR] Disconnected")
                    break
                else:
                    reply = []
                    for p in range(len(players)):
                        if p != playerId:
                            reply.append(players[p])

                    #print("Received:", data)
                    #print("Sending:", reply)

                conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("[GAME] Client Left")
    try:
        players.pop(playerId)
        print("[GAME] Disconnecting Player", playerId)
        player -= 1
    except:
        pass
    conn.close()

while True:
    conn, addr = s.accept()
    players[player] = player_list[player]
    print("[DEBUG] Connected to:", addr)
    print("[DEBUG]", players)

    start_new_thread(threaded_client, (conn, player))
    player += 1