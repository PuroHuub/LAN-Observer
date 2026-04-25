def write(ipv4_list: list, path: str):
    
    with open(path, 'w') as file_write:
        for var_ip in ipv4_list:
            file_write.write(f'{var_ip} \n')