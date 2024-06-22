# module hosts a server for website hosting

import socket


def run_server():
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 8080

    # bind socket to host and port
    s.bind((host, port))

    # listens for max 2 queued connections
    s.listen(2)
    client_socket, client_address = s.accept()
    print(f"Connection from: {client_address} has been established!")

    while True:
        # initial test
        message = "Welcome To The server"
        data = client_socket.recv(3000).decode()
        client_socket.send(message.encode())

    # don't forget to close the socket
    s.close()


run_server()
