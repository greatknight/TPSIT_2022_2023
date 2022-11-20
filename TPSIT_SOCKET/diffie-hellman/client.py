from socket import socket, AF_INET, SOCK_STREAM
import random
from common import modExp, P, G

BUFFER_SIZE = 18192

def dh(s, a):
    numero_elevato = modExp(G,a,P)
    #print(f"numero generato: {numero_elevato}")
    s.sendall(numero_elevato.to_bytes(1024,"big"))
    numeroRicevuto = s.recv(BUFFER_SIZE)
    numeroRicevutoInt = int.from_bytes(numeroRicevuto, "big")
    #print(f"numero ricevuto: {numeroRicevutoInt}")
    chiave = modExp(numeroRicevutoInt,a,P)
    print(f"chiave: {chiave}")

def runClient(host, port):
    #random.seed(27)
    a = random.randint(1,100)

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))

        dh(s, a)
        

if __name__ == "__main__":
    host = input("Inserisci l'indirizzo ip: ")
    port = int(input("Inserisci la porta: "))
    runClient(host, port)