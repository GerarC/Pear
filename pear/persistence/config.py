import os
import json
from os.path import expanduser

config = {}

class ConfigHandler:
    '''Class to handle the config.
    '''
    def __init__(self):
        self.config_path = os.path.join(
            expanduser('~'), '.config', 'pear')
        if not os.path.exists(self.config_path):
            os.makedirs(self.config_path)

    def load(self):
        '''Loads the configuration dict.

        Returns:
            config (dict): configuration.

        Raises:
            FileNotFoundError
        '''
        try:
            with open(os.path.join(self.config_path,
                'config.json')) as config_file:
                global config
                config = json.load(config_file)
                return config
        except FileNotFoundError:
            raise FileNotFoundError

    def write(self, config: dict):
        '''Writes the config in the file.

        Args:
            config (dict): Config information.
        '''
        with open(
            os.path.join(self.config_path, 'config.json'), 'w') as file:
            file.write(json.dumps(config, indent=4))

    def create_file(self):
        '''Creates the config file.
        '''
        open(os.path.join(self.config_path, 'config.json'), 'w').close()
