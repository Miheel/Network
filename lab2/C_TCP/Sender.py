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

def log_file(log_data):
    out_file = open("logfile_t.log", "w")
    out_file.write(log_data)

    out_file.close()

def split_into_packets(data, data_size):
    """split data into packets"""

    packets = [data[i:i+data_size] for i in range(0, len(data), data_size)]

    return packets

def send_packets(packets, c_socket, s_freq = 0, s_time = 0):
    """send packet"""

    data = split_into_packets(packets, 1300)
    log_data = ""

    seq_nr = 10000
    separator = ";"
    packet = 0
    
    t_end = t.time() + s_time
    start_time = t.time()

    while t.time() <= t_end and packet < len(data): #400 1000:

        end_time = t.time()
        payload = str(seq_nr) + separator + data[packet]

        print("[%.3f %d] %s" % (end_time - start_time, packet % 20, payload[0:6]))
        log_data = log_data + str("[%.3f %d] %s" % (end_time - start_time, packet % len(data), payload[0:6])) + "\n"
		
        c_socket.send(payload.encode())
			
        seq_nr = int(seq_nr) + 1		
        packet = packet + 1
		
        t.sleep(s_freq)

    log_file(log_data)

def create_socket(port, host):
    """creates a socket"""

    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)	
    client_socket.connect((host, port))
	
    return client_socket

def main():
    """main"""
	
    send_freq = 0.0189 #50/sec #0.0489 20/sec
    send_time = 20
	
    data_str = read_file("data.txt")
    client_socket = create_socket(12000, 'localhost')
	
    send_packets(data_str, client_socket, send_freq, send_time)

    client_socket.close()
    
    input("press a button")


if __name__ == "__main__":
    main()
