""" UDP Sender """

import socket as s
import time as t

def read_file(file_name):
    """
    Reads the data files
    """
    in_file = open(file_name, "r")

    data = ""
    for lines in in_file:
        data = data + lines

    return data

def split_into_packets(data, data_size):
    """
    split data into packets
    """

    packets = [data[i:i+data_size] for i in range(0, len(data), data_size)]

    return packets

def send_packets(packets, sock, addr):
    """
    send packet
    """
    data = split_into_packets(packets, 1300)

    seq_nr = 10000
    separator = ";"
    packet = 0
    #t_end = t.time() + 20
    #t.time() < t_end and
    while packet < len(data):
        payload = str(seq_nr) + separator + data[packet]
        seq_nr = int(seq_nr) + 1
        print("[", t.perf_counter(), "]", payload[0:6])
        sock.sendto(payload.encode(), addr)
        t.sleep(0.5)

def main():
    """
    main
    """
    data_str = read_file("data.txt")
    server_name = '192.168.112.97'
    server_port = 25565
    addr_info = (server_name, server_port)

    client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

    send_packets(data_str, client_socket, addr_info)

    client_socket.close()

    input()


if __name__ == "__main__":
    main()
