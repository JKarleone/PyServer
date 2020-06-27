import socketserver
from server.Handler import *
import threading


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Getting size of message
        data_size = int(self.request.recv(64).decode())
        print(data_size)

        # Getting message
        data = self.request.recv(data_size).decode()
        print(data)
        print(threading.current_thread())

        # Work with data
        answer = Handler.handle(data)

        # Correct str message length to 8 bytes
        answer_len = str(len(answer))
        while len(answer_len) != 64:
            answer_len = '0' + answer_len

        # Send answer
        self.request.sendall(str(len(answer)).encode())
        self.request.sendall(answer.encode())


class Server:
    def start(self):
        self.server = ThreadedTCPServer(('127.0.0.1', 8888), TCPHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()
        print(self.server_thread.name)

    def stop(self):
        self.server.shutdown()
