import socket as S
import datetime as dt
import os

T_STAMP = dt.datetime.now().strftime("[%X INFO]: ")
FILE_T_STAMP = dt.datetime.now().strftime("%a %b %d %X")

def read_file(file_name):
    """
    Reads the propery files
    """
    try:
        in_file = open(file_name, "r")
    except FileNotFoundError:
        in_file = open(file_name, "w+") 
        create_missing_file(in_file)

    values = []
    for lines in in_file:
        if "#" not in lines:
            properties = split(lines, "=")
            if properties.strip("\n") == "True":
                value = properties.strip("\n")
                return value
            else:
                values.append(properties.strip("\n"))

    return values

def split(line, splitter):
    """
    Splits strings
    """
    beg = ""
    end = ""
    split_flag = 0
    for index, elem in enumerate(line):
        if elem in splitter:
            split_flag = 1

        if split_flag == 0:    
            beg += elem

        if split_flag == 1:
            end += elem

    return end.lstrip(splitter)


def create_missing_file(file_in):
    """
    Creates any missign files
    """
    file_in_name = os.path.basename(file_in.name)

    if file_in_name == "server.properties":
        file_in.write("#Server properties\n#" + FILE_T_STAMP + "\n\
server-port=80\n\
server-ip=000.000.000.000\n\
object=/xxxx/xxxx.html\n\
query=?xxxxx=")

    if file_in_name == "EULA.txt":
        file_in.write("#By changing the setting below to TRUE you are indicating your eagreement to our EULA\n\
#" + FILE_T_STAMP + "\n\
eula=false\n")

def write_file(out_file_name, string="#Loggfile\n"):
    """
    logfile writer
    """
    out_file=open(out_file_name, "a") 
    out_file.write(string)
    out_file.close()

def t_stamp_print(msg=""):
    """
    prints a time stamp before all lines
    """
    print(T_STAMP, msg)
    
    log_data = T_STAMP + str(msg) + "\n"
	
    write_file("latest.log", log_data)

def main():
    """
    main function
    """
    if os.path.exists("latest.log"):
        os.remove("latest.log")
    else:
        write_file("latest.log")
        t_stamp_print("Could not find latest logfile. Creating")

    t_stamp_print("Starting client version 1.2")
    t_stamp_print("Loading properties")
	
    eula = read_file("EULA.txt")
    server_value =  read_file("server.properties") 
 
 
    if eula == "true" or "True" or "TRUE":
        port = server_value[0]
        ip = server_value[1]
        req_obj = server_value[2]
        query = server_value[3]

        t_stamp_print("Starting client on " + ip + ":" + port)      
        
        client_socket = S.socket(S.AF_INET, S.SOCK_STREAM)
        client_socket.connect((ip, int(port)))
        board_state = "xoeoexxoe" 
        
        query_line = query + board_state
		
        get_req = "GET "+ req_obj + query_line + " HTTP/1.1\r\n\
Host:" + ip + "\r\n\
Connection: close\r\n\r\n"

        client_socket.send(get_req.encode())
        data = client_socket.recv(4096).decode()
        t_stamp_print(data)
        
        client_socket.close()
        
        input()

    else:
        t_stamp_print("You need to agree to the EULA in order to run the client")
        t_stamp_print("Stopping client")



if __name__ == "__main__":
        main()
