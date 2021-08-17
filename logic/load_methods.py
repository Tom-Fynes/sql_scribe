import yaml


def get_envs_from_yaml(yaml_file):
    """
    get_envs_from_yaml function to get the envs from yaml file
    """
    windows_auth = []
    sql_auth = []
    skiped_envs = []

    with open(yaml_file, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
            for env, auth in file["environments"].items():
                if auth.get(0, True) :
                    windows_auth.append(env)
                elif auth.get(0, False):
                    sql_auth.append(env)
                else:
                    skiped_envs.append(env)
        except yaml.YAMLError as exc:
            print(exc)
    
    return windows_auth, sql_auth, skiped_envs
    

def get_file_config(config_file):
    """
    get_file_config function to get the config file
    """
    worksheets = []
    lable = []
    headers = []
    with open(config_file, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
            worksheets.append(file["worksheets"])
            lable.append(file["label"])
            headers.append(file["header"])
            return worksheets, lable, headers
        except yaml.YAMLError as exc:
            print(exc)
    
    return None
