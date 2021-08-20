import os
from colorama import Fore, Style

WAIT_TIME = 2

OUTPUT_PATH = "outputs"

ROOT_PATH = os.path.realpath(os.getcwd()) #os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

SQL_DRIVER = "SQL Server"

HIGHLIGHT_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
WARNING_COLOR = Fore.YELLOW
INTRO_COLOR = Fore.LIGHTMAGENTA_EX
DEFAULT_COLOR = Fore.WHITE
STYLE_BRIGHT = Style.BRIGHT
