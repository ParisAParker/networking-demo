import socket
from _thread import *
import sys
import json

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
# The argument '2' specifies the maximum number of queued connections
s.listen(2)
print("Waiting for a connection, Server Started") # Informing that the server is ready

# Function to handle communication wiht a connected client
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True: # Infinite loop to keep the connection alive
        try:
            data = conn.recv(2048) # Receiving data from the client (up to 2048 bytes)
            reply = data.decode("utf-8") # Decoding the received data from bytes to a string

            # If no data is received, the client has disconnected
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            # Sending the same data back to the client
            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


# Main server loop to accept and handle client connections
while True:
    conn, addr = s.accept() # Accepting a new connection from a client
    print("Connected to:", addr) 

    # Starting a new thread to handle the client
    start_new_thread(threaded_client, (conn, ))