""" UDP Receiver """

import socket as s
#import time as t

def create_socket(server_port):
    """ creates a socket """

    server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server_socket.bind(('', server_port))
    return server_socket

def err_log(err, msg):
    """ prints out packet order error """

    print("Packets out of order")
    if err == 1:
        print("Sequence too big, packet nr: ", msg)
    elif err == -1:
        print("Sequence too small, packet nr: ", msg)

def main():
    """ main """
    #server_socket = create_socket(25565)

    print("The UDP server is ready to recieve")
    message_test = ["10000;asdgj", "10001;asdgj", "10002;asdgj", "10003;asdgj", "10005;asdgj", \
"10004;asdgj", "10005;asdgj", "10007;asdgj", "10008;asdgj", "10009;asdgj"]
    seq_nr = []

    i = 0
    while i < 10:

        #print(message_test[i][0:5])
        seq_nr.append(int(message_test[i][0:5]))
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

        #message, client_address = server_socket.recvfrom(2048)
        #print(message[0:5])
        #print(client_address)
        #modifiedMessage = message.decode().upper()
        #server_socket.sendto(modifiedMessage.encode(), client_address)

    print(seq_nr)

if __name__ == "__main__":
    main()
