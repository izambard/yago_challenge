import logging

import json
import pathlib
from params import CACHE_DIR


LOGGER = logging.getLogger(__name__)

class FileStore():
    def __init__(self):
        super().__init__()
        self.root_path = pathlib.Path(CACHE_DIR)
        if not self.root_path.exists():
            self.root_path.mkdir(parents=True, exist_ok=True)
    
    def get_filepath(self, context: str)-> pathlib.Path:
        return self.root_path / context
    
    def get_all(self):
        res=[]
        for entry in self.root_path.iterdir():
            if entry.is_file():
                res.append(self.get(entry))

        return res

    def get(self, path: pathlib.Path):
        if path.exists():
            LOGGER.debug(f'FileStore loading {path}')
            try:
                with open(path, 'r') as file:
                    return json.load(file)
            except Exception as e: 
                    LOGGER.error(e)
        else:
            LOGGER.debug(f'FileStore path {path} does not exist')
            return None

    def del_(self, context: str):
        path = self.get_filepath(context)

        if path.exists():
            path.unlink()

    def save(self, context: str, resource: object):
        json_object = json.dumps(resource, indent=4)
 
        with open(self.get_filepath(context), "w") as file:
            file.write(json_object)
            LOGGER.debug(f'FileStore saved {file.name}')

