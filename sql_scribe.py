from logic.common_utils import (
    wait,
    openresults,
    createdir,
)

from logic.load_methods import (
    get_envs_from_yaml,
)

from logic.config.app_config import (
    WAIT_TIME,
    OUTPUT_PATH,
    ROOT_PATH,
)

if __name__ == '__main__': 
    # Get the envs from the yaml file
    windows_auth_servers, sql_auth_servers = get_envs_from_yaml(f"{ROOT_PATH}\config\envirnoments.yaml")
    