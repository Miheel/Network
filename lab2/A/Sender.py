""" UDP Sender """

import socket as s
import time as t
import threading as td

TIME_WAIT_SEC = 0.02'

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
    #t_end = t.time() + 20 t.time() < t_end and
    ticker = td.Event()
	start_time = t.time()
	
    while not ticker.wait(TIME_WAIT_SEC) and packet < len(data):
        end_time = t.time()
        payload = str(seq_nr) + separator + data[packet]

        print("[%.3f %d] %s" % (end_time - start_time, packet % 20, payload[0:6]))
        sock.sendto(payload.encode(), addr)
		
        seq_nr = int(seq_nr) + 1		
        packet = packet + 1
		
		#t.sleep(0.0498)

def main():
    """
    main
    """
    data_str = read_file("data.txt")
    server_name = '80.78.216.197'
    server_port = 12000
    addr_info = (server_name, server_port)

    client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

    send_packets(data_str, client_socket, addr_info)

    client_socket.close()

    input()


if __name__ == "__main__":
    main()
