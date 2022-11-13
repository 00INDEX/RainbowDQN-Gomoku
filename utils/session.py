from socket import socket
from typing import Callable


class Session(object):
    session = None
    flag = False

    def __init__(self, host: str, port: int, callback: Callable):
        super().__init__()
        self.session = socket()
        self.session.bind((host, port))
        self.session.listen(10)
        self.flag = True
        self.callback = callback
        self.listen()

    def listen(self):
        connection, address = self.session.accept()
        while self.flag:
            print('正在监听')
            data = connection.recv(1024)
            print(f"收到 {address[0]}:{address[1]} 的连接请求")
            while data[-1:] != b'#':
                data += connection.recv(1024)
            data = data[:-1]
            self.callback(data, connection)

    def __del__(self):
        if self.session is not None:
            self.session.close()
