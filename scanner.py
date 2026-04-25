import subprocess

def check_host(ip: str) -> int:
    completed = subprocess.run(f'ping {ip}')
    
    return completed.returncode

def checking(ipv: list):
    unreachable = []
    reachable = []
    
    for var_ipv in ipv:
        x = check_host(var_ipv)
        
        if x == 0:
            reachable.append(var_ipv)
        else:
            unreachable.append(var_ipv)

    return {"reachable": reachable, "unreachable": unreachable}