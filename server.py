import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.1.59"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(3)
print("Waiting for a connection, Server Started")

players = [Player(0, 0, 40, 60, (255, 0, 0)), Player(100, 100, 40, 60, (0, 0, 255)), Player(200, 200, 40, 60, (0, 255, 0))]

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
                if player == 0:
                    reply = [players[1], players[2]] 
                elif player == 1:
                    reply = [players[0], players[2]]
                else: 
                    reply = [players[0], players[1]]

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
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1