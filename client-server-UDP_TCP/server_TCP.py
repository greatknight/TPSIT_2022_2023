#!/usr/bin/env python
import sys
from socket import socket, AF_INET, SOCK_STREAM
from packet import Packet

"""server -- simple structure for a tcp server

Usage: <port> <ip_address (optinal)>

"""

BUFSIZE = 4096

class ServerOptions:
    def __init__(self, port, ip="0.0.0.0", *args):
        """Constructor

        Params
        ------
        ip: ip address the server should bind to
        port: port the server should bind to
        """
        # TODO: validation
        self.ip = ip
        self.port = int(port)

    def get_socket(self):
        """a socket is a tuple (ip, port)"""
        return self.ip, self.port

def handle_client(client):
    """Receive and send data from/to the client

    Params:
    client: socket of the connected client
    """
    go_on = True

    while go_on:
        data = client.recv(BUFSIZE)
        if len(data) == 0:
            go_on = False
        else:
            # TODO: see comment in client.py when s.send is called
            print(data.decode('utf-8'))

    client.close()

def main(args):
    """The server starts here

    Params
    ------
    args: command line arguments
    """

    options = ServerOptions(*args[1:]) # cli arguments, less the program name

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(options.get_socket())
        print(f"Server bound to {options.get_socket()}")
        s.listen()

        while True:
            print(f"Wait for a new connection")
            client, client_address = s.accept()
            print(f"New connection from {client_address}")
            handle_client(client)
            print(f"{client_address} ended connection")


if __name__ == "__main__":
    main(sys.argv)