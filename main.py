import logger_config
import reader
import validator
import logging

logger = logging.getLogger(__name__)

ascii_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

def main():
    logger_config.loggingSet()
    
    print(f"{ascii_snek}welcome to SnakeObserver")
    
    readed_ipaddress = reader.read_file()
    logger.debug(f"Getted data: {readed_ipaddress}")
    
    validated_data = validator.validation_ipaddress(readed_ipaddress)
    print(f"{validated_data}")

if __name__ == "__main__":
    main()