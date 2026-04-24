import subprocess

def check_host(ip: str) -> None:
    subprocess.run(f'ping {ip}')

def checking(ipv: list):
    for var_ipv in ipv:
        check_host(var_ipv)