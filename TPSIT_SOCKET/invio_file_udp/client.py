from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024

def chatClient(ip, port):
    with socket(AF_INET, SOCK_DGRAM) as s:
        f = open("pdf.pdf", "rb")
        buffer = f.read()
        #print(buffer)
        i = 0
        try:
            while buffer[i * 4096 + 4095]:
                message = buffer[i * 4096: i * 4096 + 4095]
                s.sendto(message, (ip, port))
                i += 1
        except:
            message = buffer[i * 4096:]
        s.sendto(message, (ip, port))


if __name__ == "__main__":
    ip = input("Inserisci ip: ")
    port = int(input("Inserisci porta: "))
    chatClient(ip,port)