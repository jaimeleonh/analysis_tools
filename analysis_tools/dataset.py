import os
from subprocess import call
from utils import randomize
from base_object import BaseObject
from process import Process


class Dataset(BaseObject):
    def __init__(self, name, folder, process, *args, **kwargs):
        self.name = name
        assert isinstance(process, Process)
        self.process = process
        self.folder = folder
        self.prefix = kwargs.pop("prefix", None)
        super(Dataset, self).__init__(*args, **kwargs)

    def locate_files(self):
        if not self.prefix:
            return os.listdir(self.folder)
        else:
            filename = randomize("./tmp") + ".txt"
            rc = call("xrdfs {} ls {} > {}".format(self.prefix, self.folder, filename), shell = True)
            if rc == 0:
                with open(filename) as f:
                    files = [file.strip() for file in f.readlines()]
                os.remove(filename)
                return files
    
    def get_files(self):
        return self.locate_files()
