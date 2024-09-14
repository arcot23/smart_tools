import os
import yaml

def get_config(config_file):
    if not os.path.isabs(config_file): config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                        config_file)

    if not os.path.exists(config_file):
        print(f"Config file `{config_file}` missing.")
        return 1

    with open(config_file, 'r') as f:
        configs = yaml.safe_load(f)

    return configs