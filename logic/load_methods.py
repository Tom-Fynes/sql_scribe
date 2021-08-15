import yaml


def get_envs_from_yaml(yaml_file):
    """
    get_envs_from_yaml function to get the envs from yaml file
    """
    windows_auth = []
    sql_auth = []

    with open(yaml_file, 'r') as stream:
        try:
            file = yaml.safe_load(stream)
            for env, auth in file["environments"].items():
                if auth.get(0, True) :
                    windows_auth.append(env)
                else:
                    sql_auth.append(env)
        except yaml.YAMLError as exc:
            print(exc)
    
    return windows_auth, sql_auth
    
