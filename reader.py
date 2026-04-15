def read_file():
    file = "c:/Users/Hp/LANobserver/targets.txt"
    
    file_open = open(file, 'r')
    
    list_file = file_open.read().strip().split()
    
    file_open.close()
    
    return list_file