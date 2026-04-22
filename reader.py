import pathlib

def read_file():
    file = pathlib.Path("targets.txt")
    
    with open(file, 'r') as open_file:
        list_file = open_file.read().strip().split()
    
    return list_file