import socket
import pathlib

def get_ip():
    file = pathlib.Path("targets.txt")
    
    host_name = ''
    address_list = socket.getaddrinfo(host_name, None)
    
    ip_list = []
    
    for address in address_list:
        ip_list.append(address[4][0])
        
    with open(file, 'w') as file_write:
        for var_ip in ip_list:
            file_write.write(f'{var_ip} \n')