""" TCP Sender """

import socket as s
import time as t

def read_file(file_name):
    """Reads the data files"""

    in_file = open(file_name, "r")

    data = ""
    for lines in in_file:
        data = data + lines

    in_file.close()
    return data

def split_into_packets(data, data_size):
    """split data into packets"""

    packets = [data[i:i+data_size] for i in range(0, len(data), data_size)]

    return packets

def send_packets(data_str, c_socket, s_freq = 0, s_time = 0):
    """send packet"""

    data = split_into_packets(data_str, 1300)
    packet = 0

    t_end = t.time() + s_time
    start_time = t.time()

    while t.time() <= t_end and packet < len(data):

        end_time = t.time()
        payload = data[packet]
        #print("[%.3f %d %d] %s" % (end_time - start_time, packet % 50, packet, payload[0:6]))
        c_socket.sendall(payload.encode())

        packet = packet + 1

        t.sleep(s_freq)

def create_socket(port, host):
    """creates a socket"""

    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.connect((host, port))

    return client_socket

def main():
    """main"""

    send_freq = 0.03 #50/sec0.07 #20/sec 1
    send_time = 20

    data_str = read_file("data.txt")
    client_socket = create_socket(12000, '80.78.216.148')

    send_packets(data_str, client_socket, send_freq, send_time)

    client_socket.close()

    input("press a button")


if __name__ == "__main__":
    main()
