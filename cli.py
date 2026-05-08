import argparse
import start

def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('argument')
    
    argument = parser.parse_args()
    
    print(parser.parse_args())
    
    if argument.argument == "findIPV4" or argument.argument == "f":
        start.find_ipv4()
    elif argument.argument == "writeIPV4" or argument.argument == "w":
        start.write_ipv4()
    elif argument.argument == "readIPV4" or argument.argument == "r":
        start.read_ipv4()
    elif argument.argument == "readFile" or argument.argument == "rf":
        start.read_file()
    elif argument.argument == "help" or argument.argument == "h":
        start.help()
    else:
        print("неизвестная команда")