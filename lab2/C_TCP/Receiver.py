""" TCP Receiver """

import socket as s
import time as t

def create_socket(server_port):
    """creates a socket"""

    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    return server_socket

def err_log(err, msg):
    """prints out packet order error"""

    print("Packets out of order")
    if err == 1:
        print("Sequence too big, packet nr: ", msg) 
    elif err == -1:
        print("Sequence too small, packet nr: ", msg)

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
                print("[", client_address, t.perf_counter(), "]", message[0:5])
                seq_nr.append(int(message[0:5]))
                
                if i > 0:
                    prev_seq_nr = seq_nr[0]
                    new_seq_nr = seq_nr[i]
                    prev_seq_nr = prev_seq_nr + i

                    #om de nyaste är större (två eller mer) än den tidigare
                    if new_seq_nr > prev_seq_nr:
                        err_log(1, i + 1)

                    #om dew nyaste är mindre an de tidagaste
                    elif new_seq_nr < prev_seq_nr:
                        err_log(-1, i + 1)

                    i = i + 1
            else:
                in_loop = False

        conn_sock.close()

    print(seq_nr)

if __name__ == "__main__":
    main()
