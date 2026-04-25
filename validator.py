import ipaddress

def validate_ip_addresses(list_ipv4: list) -> dict:
    validate_data = []
    invalid_data = []
    for var_ipv4 in list_ipv4:
        try:
            examination = ipaddress.ip_address(var_ipv4)
            validate_data.append(var_ipv4) 
        except ValueError:
            invalid_data.append(var_ipv4)
            
    return {"valid": validate_data, "invalid": invalid_data}