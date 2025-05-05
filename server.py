import socket
from _thread import *
from player import Player
from settings import *
import json
import pickle

# Load in config.json
with open("config.json", 'r') as file:
    config = json.load(file)

# Creating a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Load in variables from config.json
server = config['server']
port = config['port']

# Attempting to bind the server's IP address and port to the socket
try:
    s.bind((server,port))
except socket.error as e:
    print(str(e)) # If an error ocurs, it is converted to a string and printed

# Configuring the socket to listen for incoming connections
s.listen(2)
print("Waiting for a connection, Server Started") # Informing that the server is ready

players = [Player(0, 0, 50, 50, RED), Player(100, 100, 50, 50, GREEN)]

# Function to handle communication with a connected client
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True: # Infinite loop to keep the connection alive
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data            

            # If no data is received, the client has disconnected
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                # print("Received: ", data)
                # print("Sending: ", reply)

            # Sending the same data back to the client
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

# Main server loop to accept and handle client connections
while True:
    conn, addr = s.accept() # Accepting a new connection from a client
    print(f"Player {currentPlayer} is connected to: ", addr)

    # Starting a new thread to handle the client
    start_new_thread(threaded_client, (conn, currentPlayer))
    print(currentPlayer)
    currentPlayer += 1