import socketserver
from Handler import *
from data.User import User
from data.UserType import UserType
from data.Film import Film
from data.FilmScoreByUser import FilmScoreByUser
from data.Person import Person
from data.Filmmaker import Filmmaker
from data.Actor import Actor
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


# Main loop
if __name__ == '__main__':
    # Create tables if they're not exist
    UserType.create_table()
    User.create_table()
    Person.create_table()
    Film.create_table()
    FilmScoreByUser.create_table()
    Actor.create_table()
    Filmmaker.create_table()

    if UserType.count() == 0:
        UserType.add("User")
        UserType.add("Admin")

    server = ThreadedTCPServer(('127.0.0.1', 8888), TCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    print(server_thread.name)
