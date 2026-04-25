import main

def starting():
    print("выберите две доступные вам функции:")
    print("--findIPV4")
    print("--writeIPV4")
    print("--updateIPV4")
    print("--readIPV4")
    print("--readFile")
    print("--help")
    command = input()
    
    if command == "--findIPV4":
        main.find_ipv4()
    elif command == "--writeIPV4":
        main.write_ipv4()
    elif command == "--updateIPV4":
        pass
    elif command == "--readIPV4":
        main.read_ipv4()
    elif command == "--readFile":
        main.read_file()
    elif command == "--help":
        help()
    else:
        print("неизвестная команда")
        
def help():
    print("--findIPV4 этой командой программа ищет все айпи в вашей LAN \n--writeIPV4 этой командой программа записывает ваши IPV4 \n--readIPV4 этой командой программа читает ранее записанные айпи \n--readFile этой командой программа читает айпишники из вашего файла путь котого вы указываете сами и не только название файла с абсолютным путем но и .txt указать должны")