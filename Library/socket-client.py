
import socket

class soc:
    def __init__(self, url, port):
        self.url = url
        self.port = port
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((url, port))
        except:
            exit(1)

    def recv(self, len=2048, decode=True):
        data = self.s.recv(len)
        decoded = data.decode('utf-8')
        print('[+] recieve:', decoded)
        if decode:
            return decoded
        else:
            return data
    
    def recvuntil(self, c, decode=True):
        data = b''
        while True:
            a = self.s.recv(1)
            data += a
            if c == a:
                break
        decoded = data.decode('utf-8')
        print('[+] recieve:', decoded)
        if decode:
            return decoded
        else:
            return data

    def send(self, data):
        if isinstance(data, bytes):
            print('[+] send:', data.decode('utf-8'))
            self.s.sendall(data)
        else:
            print('[+] send:', data)
            self.s.sendall(data.encode('utf-8'))

if __name__ == '__main__':
    ip = '172.217.31.131'
    port = 443
    s = soc(ip, port)
    s.read()