class Process():
    def __init__(self, name, label, **kwargs):
        self.name = name
        self.label = label
        self.parent_process = None if "parent_process" not in kwargs else kwargs["parent_process"]
        self.subprocesses = []
        self.color = (0, 0, 0) if "color" not in kwargs else kwargs["color"]
    
    def add_subprocess(self, process):
        self.subprocesses.append(process)
    
    
        