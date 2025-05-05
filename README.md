# Networking Demo

This project is a learning exercise to understand the basics of Python's `socket` library and how to create an online/multiplayer game using `pygame`.

## Overview

The project consists of a simple client-server architecture:
- **Server**: Handles incoming connections and facilitates communication between clients.
- **Client**: Connects to the server and exchanges data.

The goal is to use this foundation to build a multiplayer game with `pygame`.

## Features

- Basic socket programming with Python.
- Multi-threaded server to handle multiple client connections.
- Configuration management using a `config.json` file.
- Echo server functionality as a starting point for multiplayer communication.

## Technologies Used

- **Python**: Core programming language.
- **Socket Library**: For networking and communication.
- **Pygame**: (Planned) For creating the multiplayer game.

Create a `config.json` file in the project directory with the following structure:

```json
{
    "server": "server_ip",
    "port": port_number
}
```
## Resources
**Socket library documentation**: [Documentation](https://docs.python.org/3/library/socket.html#socket-objects)