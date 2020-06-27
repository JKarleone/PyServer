import socket


class Request:
    @staticmethod
    def request(request_body):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(('localhost', 8888))
        except:
            sock.close()
            return 'can\'t connect to server'
        message_len = str(len(request_body))
        while len(message_len) != 64:
            message_len = '0' + message_len

        sock.send(message_len.encode())
        sock.send(request_body.encode())

        result_size = int(sock.recv(64).decode())
        result = sock.recv(result_size).decode()

        sock.close()

        return result
