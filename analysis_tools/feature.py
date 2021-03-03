class Feature():
    def __init__(self, name, expression, **kwargs):
        self.name = name
        self.expression = expression
        self.selection = None if "selection" not in kwargs else kwargs["selection"]
        self.binning = (10, 0, 1) if "binning" not in kwargs else kwargs["binning"]
        
