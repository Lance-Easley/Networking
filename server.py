import socket
from _thread import *
import sys
from player import Player, Absent
import pickle

server = "192.168.1.59"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(9)
print("Waiting for a connection, Server Started")

player_list = [
    Player(0, 0, 40, 60, (255, 0, 0)), Player(100, 0, 40, 60, (0, 0, 255)), Player(200, 0, 40, 60, (0, 255, 0)), 
    Player(0, 100, 40, 60, (255, 0, 0)), Player(100, 100, 40, 60, (0, 0, 255)), Player(200, 100, 40, 60, (0, 255, 0)), 
    Player(0, 200, 40, 60, (255, 0, 0)), Player(100, 200, 40, 60, (0, 0, 255)), Player(200, 200, 40, 60, (0, 255, 0)), 
    ]

players = []

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) # Truanced: increase number
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = []
                for p in range(len(players)):
                    if p != player:
                        reply.append(players[p])

                print("Received:", data)
                print("Sending:", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost Connestion")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    players.append(player_list[currentPlayer])
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1