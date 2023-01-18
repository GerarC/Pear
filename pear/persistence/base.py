import json
import os
from os.path import expanduser


class JsonDB():
    '''Base Class to make Json databases.

    Args:
        schema (Union[list, dict]): base schema of the database.
        filename (str): name of the json file.
        dir (dir, Optional): path to the json file. Defaults to \'\'
    '''

    def  __init__(self, schema, filename, dir=''):
        '''Base Class to make Json databases.

        Args:
            schema (Union(list, dict)): base schema to create the database.
            filename (str): name of the json file.
            dir (dir, Optional): path to the json file.
        '''
        if dir == '':
            self._filename = os.path.join(
                expanduser('~'),
                '.config',
                'pear',
                'library',
                f'{filename}.json'
            )
        else:
            self._filename = os.path.join(dir, f'{filename}.json')

        try:
            file = open(self._filename)
            file.close()
        except IOError:
            with open(self._filename, mode='w', encoding='utf-8') as j_file:
                json.dump(schema, j_file, indent = 4)

    def read(self):
        '''Opens the json file and load all the information.

        Returns:
            data (Union[list, dict]): iterable of the file information.
        '''
        with open(self._filename, 'r') as f:
            data = json.load(f)
        return data

    def write(self, data) -> None:
        '''Dumps the given data in the database.

        Args:
            data (Union[list, dict]): an iterable with valid json information.
        '''
        with open(self._filename, 'w') as f:
            f.seek(0)
            json.dump(data, f, indent = 4)
            f.truncate()

    def append(self, val, desc=None) -> None:
        '''Appends the given value to the database.

        Args:
            val (Union[list, dict]): an iterable with valid json information.
            desc (Union[int, str, bool]): a key that's used if the data is a dictionary.
        '''
        with open(self._filename, 'r+') as f:
            data = json.load(f)
            if desc is None:
                if type(data) == list:
                    data.append(val)
            elif type(data) == dict:
                    data[desc].append(val)
            f.seek(0)
            json.dump(data, f, indent = 4)

    def delete_by_index(self, index: int):
        '''If the database is a list of objects deletes the object of the given index else it does nothing.

        Args:
            index (int): the object index.

        Returns:
            item (dict, list): the items that was delete form the database.
        '''
        data = self.read()
        if type(data) == list:
            deleted = data.pop(index)
            self.write(data)
            return deleted
