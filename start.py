import reader
import validator
import writer
import scanner
import writer_user

def starting():
    print("выберите две доступные вам функции:")
    print("--findIPV4")
    print("--writeIPV4")
    print("--updateIPV4")
    print("--readIPV4")
    print("--readFile")
    print("--help")
    
    return input().strip()
    
        
def help():
    print("--findIPV4 этой командой программа ищет все айпи в вашей LAN \n--writeIPV4 этой командой программа записывает ваши IPV4 \n--readIPV4 этой командой программа читает ранее записанные айпи \n--readFile этой командой программа читает айпишники из вашего файла путь котого вы указываете сами и не только название файла с абсолютным путем но и .txt указать должны")
    
    

def find_ipv4():
    writer.get_ip()
    
    readed_ipaddress = reader.read_file("discovered_targets.txt")
    print(f"Getted data: {readed_ipaddress}")
    
    validated_data = validator.validate_ip_addresses(readed_ipaddress)
    print(f"{validated_data}")
    
    #scanner.check_host('192.168.1.1')
    #scanner.check_host('127.0.0.1')
    
    scannered_ipv = scanner.checking(validated_data['valid'])
    
    print(scannered_ipv)
    
def write_ipv4():
    list_ipv4 = []
    
    while True:
        input_ipv = input("введите 1 айпи или напишите end чтобы закочить запись: ")
        if input_ipv == "end":
            break
        else:
            list_ipv4.append(input_ipv)
            
    print(list_ipv4)
    
    writer_user.write(list_ipv4, "writed_targets.txt")
    
    readed_ipaddress = reader.read_file("writed_targets.txt")
    
    validated_data = validator.validate_ip_addresses(readed_ipaddress)
    
    print(f"{validated_data}")
    
    scannered_ipv = scanner.checking(validated_data['valid'])
    print(scannered_ipv)

def update_ipv4():
    pass #в разработке (навсегда)

def read_ipv4():
    readed_ipaddress = reader.read_file("writed_targets.txt")
    
    validated_data = validator.validate_ip_addresses(readed_ipaddress)
    
    print(f"{validated_data}")
    
    scannered_ipv = scanner.checking(validated_data['valid'])
    print(scannered_ipv)
    
def read_file():
    path = input("введите абсолютный путь до файла: ")
    
    readed_ipaddress = reader.read_file(path)
    
    validated_data = validator.validate_ip_addresses(readed_ipaddress)
    
    print(f"{validated_data}")
    
    scannered_ipv = scanner.checking(validated_data['valid'])
    print(scannered_ipv)