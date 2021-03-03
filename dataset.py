import os
from subprocess import call
from utils import randomize

from process import Process

class Dataset():
    def __init__(self, name, folder, process, **kwargs):
        self.name = name
        if not isinstance(process, Process):
            raise ValueError("{} is not an instance of class Process".format(process))
        self.process = process
        self.folder = folder
        self.prefix = None if "prefix" not in kwargs else kwargs["prefix"]

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
