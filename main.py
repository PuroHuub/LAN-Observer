import logging
import reader
import validator

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG, #большими потому что константа 
    filename="py_log.log",
    filemode="w", 
    ) 

FORMATTER = logging.Formatter(
    "%(message)s"
    )

console_logger = logging.StreamHandler()
console_logger.setFormatter(FORMATTER)

logger.addHandler(console_logger)

ascii_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

def main():
    logger.info(f"{ascii_snek}welcome to SnakeObserver")
    readed_ipaddress = reader.read_file()
    logger.info(f"{readed_ipaddress}")
    
    result_validator = validator.read_ipaddress(readed_ipaddress)
    logger.info(f"Validate and Invaid data: {result_validator}")


if __name__ == "__main__":
    main()