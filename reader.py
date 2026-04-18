import pathlib

def read_file():
    file = pathlib.Path("targets.txt")
    
    file_open = open(file, 'r')
    
    list_file = file_open.read().strip().split()
    
    file_open.close()
    
    return list_file