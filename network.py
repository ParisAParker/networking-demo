import socket
import json

# Load in config.json
with open('config.json', 'r') as file:
    config = json.load(file)

# Load in variables from config.json
server = config['server']
port = config['port']

# Create class that's responsible for connecting to the server
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass