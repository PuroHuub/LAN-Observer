import logger_config
import logging
import start
import cli

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
    
    cli.parse_args()
if __name__ == "__main__":
    main()