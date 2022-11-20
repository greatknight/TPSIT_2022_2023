# | 1 byte (#username) | username | 2 byte (#message) | message

class Packet:
    def __init__(self, username, message):
        # validazione
        self.username = username
        self.message = message
    
    # Converte un oggetto Packet in bytes
    def to_bytes(self):
        username_bytes = self.username.encode('utf8')
        buffer = len(username_bytes).to_bytes(1, 'big')
        buffer = buffer + username_bytes
        message_bytes = self.message.encode('utf8')
        buffer = buffer + len(message_bytes).to_bytes(2, 'big')
        buffer = buffer + message_bytes
        return buffer
    
    @staticmethod
    def from_bytes(buffer):
        num = buffer.decode("utf8")
        num = int(num)
        return num

if __name__ == "__main__":
    #run_tests()
    pass