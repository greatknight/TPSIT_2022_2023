#!/usr/bin/env python
import sys
from socket import socket, AF_INET, SOCK_STREAM

"""client -- simple structure for a tcp client

Usage: <ip_address> <port>

"""

class ClientOptions:
    def __init__(self, ip, port, *args):
        """Constructor

        Params
        ------
        ip: ip address of the server
        port: port on the server
        """
        # TODO: validation
        self.ip = ip
        self.port = int(port)

    def get_socket(self):
        """a socket is a tuple (ip, port)"""
        return self.ip, self.port

def ask_command():
    return input("$> ")

def main(args):
    """The client starts here

    Params
    ------
    args: command line arguments
    """

    options = ClientOptions(*args[1:]) # cli arguments, less the program name
    go_on = True

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(options.get_socket())

        while go_on:
            # TODO: to send more complex data types write
            #       his own class with serialization and
            #       deserialization
            cmd = ask_command()

            if cmd == "exit":
                go_on = False
            else:
                s.send(cmd.encode('utf-8'))


if __name__ == "__main__":
    main(sys.argv)