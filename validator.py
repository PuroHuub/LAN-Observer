import ipaddress

def read_ipaddress(ipv4: list) -> ipaddress.IPv4Address:
    validate_data = []
    invalid_data = []
    for list_ipv4 in ipv4:
        try:
            examination = ipaddress.ip_address(list_ipv4)
            validate_data.append(list_ipv4) 
        except ValueError:
            invalid_data.append(list_ipv4)
            
    return validate_data, invalid_data