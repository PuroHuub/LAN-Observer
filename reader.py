import pathlib

def read_file():
    file = pathlib.Path("targets.txt")
    
    with open(file, 'r') as open_file:
        list_file = [line.strip() for line in open_file if line.strip()]
    
    return list_file