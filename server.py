import socket
from _thread import *
import sys
import json

# Load in config.json
with open("config.json", 'r') as file:
    config = json.load(file)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Load in variables from config.json
server = config['server']
port = config['port']

# Bind server and port to the socket
# The port could be in use for something else
try:
    s.bind((server,port))
except socket.error as e:
    str(e)

# Listening for connections on that port
s.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, ))