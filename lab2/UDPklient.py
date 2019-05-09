from socket import *
import time as t

def read_file(file_name):
    """
    Reads the propery files
    """
    in_file = open(file_name, "r")

    data = ""
    for lines in in_file:
        data = data + lines

    return data

def split_into_packets(data, data_size):

    packets = [data[i:i+data_size] for i in range(0, len(data), data_size)]

    return packets

def send_packets(packets, sock, addr):
    """
    """
    data = split_into_packets(packets, 1300)

    seq_nr = 10000
    separator = ";"
    packet = 0
    i = 0
    t_end = t.time() + 20
    #for packet in data:
    while t.time() < t_end and packet < len(data):
        payload = str(seq_nr) + separator + data[packet]
        seq_nr = int(seq_nr) + 1			
        print("[", t.perf_counter(), "]", payload[0:6])
        sock.sendto(payload.encode(), addr)
        t.sleep(0.05)

def main():
    """
    """
    data_str = read_file("data.txt")
    serverName = '80.78.216.191'
    serverPort = 12000
    addrinfo = (serverName, serverPort)
	
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    send_packets(data_str, clientSocket, addrinfo)

    clientSocket.close()

    input()


if __name__ == "__main__":
    main()

