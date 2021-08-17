from colorama import init, Fore
from logic.common_utils import (
    wait,
    openresults,
    createdir,
)

from logic.load_methods import (
    get_envs_from_yaml,
    get_file_config,
)

from logic.config.app_config import (
    WAIT_TIME,
    OUTPUT_PATH,
    ROOT_PATH,
    WARNING_COLOR,
    ERROR_COLOR,
    HIGHLIGHT_COLOR,
    DEFAULT_COLOR,
    STYLE_BRIGHT,
    INTRO_COLOR,
)


init(convert=True, autoreset=True)

if __name__ == '__main__': 
    # Get the envs from the yaml file
    
    print(f"{INTRO_COLOR}Welcome to SQL Scribe")
    windows_auth_servers, sql_auth_servers, skiped_servers = get_envs_from_yaml(f"{ROOT_PATH}\config\envirnoments.yaml")
    worksheets, label, header = get_file_config(f"{ROOT_PATH}\config\excel_config.yaml")

    print(f"{HIGHLIGHT_COLOR}{str(len(windows_auth_servers))}{DEFAULT_COLOR} windows auth servers found")
    print(f"{HIGHLIGHT_COLOR}{str(len(sql_auth_servers))}{DEFAULT_COLOR} sql server auth servers found")
    print(f"{HIGHLIGHT_COLOR}{str(len(skiped_servers))}{DEFAULT_COLOR} server skipped due to invalid config")
    