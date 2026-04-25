import pathlib

def read_file(path: str):
    file = pathlib.Path(path)
    
    with open(file, 'r') as open_file:
        list_file = [line.strip() for line in open_file if line.strip()]
    
    return list_file