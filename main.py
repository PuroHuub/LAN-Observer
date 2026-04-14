import logging

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

if __name__ == "__main__":
    main()