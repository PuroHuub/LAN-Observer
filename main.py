import logger_config
import reader
import validator
import logging
import writer
import scanner

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
    
    writer.get_ip()
    
    readed_ipaddress = reader.read_file()
    logger.debug(f"Getted data: {readed_ipaddress}")
    
    validated_data = validator.validate_ip_addresses(readed_ipaddress)
    print(f"{validated_data}")
    
    #scanner.check_host('192.168.1.1')
    #scanner.check_host('127.0.0.1')
    
    scannered_ipv = scanner.checking(validated_data['valid'])
    
    print(scannered_ipv)

if __name__ == "__main__":
    main()