from socket import AF_INET,socket,SOCK_DGRAM,SOL_SOCKET,SO_BROADCAST
from packet import Packet
def chat_Client(HOST,PORT,username):
    with socket(AF_INET,SOCK_DGRAM) as s:
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        while True:
            msg=input("inserire messaggio:")
            p=Packet(username,msg)
            s.sendto(p.to_bytes(),(HOST,PORT))
            print("messaggio inviato")


if __name__ == '__main__':
    username=input("inserire nome:")
    HOST=input("inserire l'indirizzo ip dell'host:")
    PORT=int(input("inserire porta"))
    chat_Client(HOST, PORT,username)