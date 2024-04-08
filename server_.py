#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""

from socket import *
from threading import Thread
import numpy as np


# def make_packet(msg_type,msg):
#     packet=bytearray()
#     packet.extend(msg_type[i] for i in range(len(msg_type)))
#     packet.extend(msg[i] for i in range(len(msg)))
#     return packet

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        msg_type = b'type1'
        msg = b'Greetings from the {Project:Phase_2}! Now type your name and press enter!'
        client.send(msg_type + msg)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(b'type1' + welcome.encode())

    msg = "%s has joined the chat!" % name
    general_info = b'type1' + msg.encode()
    broadcast(general_info)
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            name1 = name + str(len(name)) * (20 - len(name))
            broadcast(msg, name1, client)
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix="", count=None):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock, ind_name in clients.items():
        if (ind_name + str(len(ind_name)) * (20 - len(ind_name))) == prefix:
            print(ind_name)
            continue
        sock.send(bytes(prefix, "utf8") + msg)
        # sock.send(make_packet(prefix.encode(),msg))


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 2048
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()