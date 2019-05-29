""" TCP Receiver """

import socket as s
import time as t

def create_socket(server_port):
    """creates a socket"""

    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    return server_socket

def main():
    """main"""

    seq_nr = []
    in_loop = True
    i = 0
    server_socket = create_socket(12000)

    while True:
        print('waiting for a connection')
        conn_sock, client_address = server_socket.accept()
        in_loop = True

        while in_loop == True:
            message = conn_sock.recv(2048).decode()
            if message:
                print("[", client_address, t.perf_counter(), "] size", len(message), message[0:10])


            else:
                in_loop = False

        conn_sock.close()

    print(seq_nr)

if __name__ == "__main__":
    main()
