import socketserver
import threading
from data.User import User
from data.UserType import UserType
from data.Film import Film
from data.FilmScoreByUser import FilmScoreByUser
from data.Person import Person
from data.Filmmaker import Filmmaker
from data.Actor import Actor


def authentication(data):
    try:
        login = data.split(':')[1]
        password = data.split(':')[2]
    except ValueError:
        return 'error'
    return 'ok' if User.auth(login, password) else 'error'


def user_handler(data):
    try:
        command = data.split(':')[1]
    except ValueError:
        return 'bad method name'

    if command == 'add':
        try:
            split_data = data.split(':')
            login = split_data[2]
            password = split_data[3]
            name = split_data[4]
        except ValueError:
            return 'error'

        User.add(login, password, name)
        return 'added'

    return 'error'


def film_handler(data):
    try:
        command = data.split(':')[1]
    except ValueError:
        return 'bad method'

    if command == 'add':
        pass


def make_decision(data):
    try:
        table_name = data.split(':')[0]
    except ValueError:
        return 'error'

    if table_name == 'user':
        return user_handler(data)

    if table_name == 'auth':
        return authentication(data)

    return 'error'


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Getting size of message
        data_size = int(self.request.recv(8).strip())

        # Getting message
        data = self.request.recv(data_size).strip().decode()

        # Work with data
        answer = make_decision(data)

        # Correct str message length to 8 bytes
        answer_len = str(len(answer))
        while len(answer_len) != 8:
            answer_len = '0' + answer_len

        # Send answer
        self.request.sendall(str(len(answer)).encode('utf-8'))
        self.request.sendall(answer.encode('utf-8'))


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

    # if UserType.count() == 0:
    #     UserType.add()
    
    with socketserver.TCPServer(('127.0.0.1', 8888), TCPHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
