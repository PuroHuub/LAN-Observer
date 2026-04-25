import logger_config
import logging
import start

logger = logging.getLogger(__name__)

ascii_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""


def main():
    logger_config.logging_setup()
    
    print(f"{ascii_snek}welcome to SnakeObserver")
    
    command = start.starting()
    
    if command == "--findIPV4":
        start.find_ipv4()
    elif command == "--writeIPV4":
        start.write_ipv4()
    elif command == "--updateIPV4":
        pass
    elif command == "--readIPV4":
        start.read_ipv4()
    elif command == "--readFile":
        start.read_file()
    elif command == "--help":
        start.help()
    else:
        print("неизвестная команда")

if __name__ == "__main__":
    main()