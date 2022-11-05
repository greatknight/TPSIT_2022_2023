from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 131072

mystr = "ciao"

HOST = "0.0.0.0"
PORT = 5000

def chatServer():
    go_on = True
    with socket (AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        txt = b""
        print("Server in ascolto")
        while go_on == True:
            msg = s.recvfrom(BUFFER_SIZE)
            if len(msg[0]) == 4096:
                txt = txt + msg[0]
            else:
                go_on = False
        txt = txt + msg[0]
        f = open("pdf_result.pdf", "wb")
        f.write(txt)
        print("done")

if __name__ == "__main__":
    chatServer()