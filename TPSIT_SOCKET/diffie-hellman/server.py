from socket import socket, AF_INET, SOCK_STREAM
import random
from common import modExp, P, G

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 18192

def dh(client, a):
    numero_elevato = modExp(G,a,P)
    #print(f"numero generato: {numero_elevato}")
    client.sendall(numero_elevato.to_bytes(1024,"big"))
    numeroRicevuto = client.recv(BUFFER_SIZE)
    numeroRicevutoint = int.from_bytes(numeroRicevuto, "big")
    #print(f"numero ricevuto: {numeroRicevutoint}")
    chiave = modExp(numeroRicevutoint,a,P)
    print(f"chiave: {chiave}")

def runServer():
    #random.seed(4)
    a = random.randint(1,100)

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        print("Server in ascolto")
        
        client, clientAddress = s.accept()

        dh(client, a)

        

if __name__ == "__main__":
    runServer()