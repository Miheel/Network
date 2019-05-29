""" UDP Sender """

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

def log_file(log_data):
    out_file = open("logfile_sleep_0.log", "w")
    out_file.write(log_data)

    out_file.close()

def split_into_packets(data, data_size):
    """split data into packets"""

    packets = [data[i:i+data_size] for i in range(0, len(data), data_size)]

    return packets

def send_packets(packets, sock, addr):
    """send packet"""
	
    data = split_into_packets(packets, 1300)
    log_data = ""

    seq_nr = 10000
    separator = ";"
    packet = 0
    
    t_end = t.time() + 20
    start_time = t.time()

    while packet < len(data):
        end_time = t.time()
        payload = str(seq_nr) + separator + data[packet]

        #print("[%.3f %d] %s" % (end_time - start_time, packet % 20, payload[0:6]))
        log_data = log_data + str("[%.3f %d] %s" % (end_time - start_time, packet % len(data), payload[0:6])) + "\n"

        sock.sendto(payload.encode(), addr)
		
        seq_nr = int(seq_nr) + 1		
        packet = packet + 1
        t.sleep(0.0498)

    log_file(log_data)

def main():
    """main"""
	
    data_str = read_file("data.txt")
    server_name = '80.78.216.148'
    server_port = 12000
    addr_info = (server_name, server_port)

    client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

    send_packets(data_str, client_socket, addr_info)

    client_socket.close()
    
    input("press a button")


if __name__ == "__main__":
    main()
