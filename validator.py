import ipaddress

def validation_ipaddress(ipv4: list) -> ipaddress.IPv4Address:
    validate_data = []
    invalid_data = []
    for var_ipv4 in ipv4:
        try:
            examination = ipaddress.ip_address(var_ipv4)
            validate_data.append(var_ipv4) 
        except ValueError:
            invalid_data.append(var_ipv4)
            
    return {"valid": validate_data, "invalid": invalid_data}