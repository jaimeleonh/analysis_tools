from base_object import BaseObject


class Process(BaseObject):
    def __init__(self, name, label, *args, **kwargs):
        self.name = name
        self.label = label
        self.subprocesses = []
        self.parent_process = kwargs.pop("parent_process", None)
        self.color = kwargs.pop("color", (0, 0, 0))
        super(Process, self).__init__(*args, **kwargs)
    
    def add_subprocess(self, process):
        self.subprocesses.append(process)
    
    def get_color(self):
        return self.color
        
