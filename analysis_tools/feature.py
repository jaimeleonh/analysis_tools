from base_object import BaseObject


class Feature(BaseObject):
    def __init__(self, name, expression, **kwargs):
        self.name = name
        self.expression = expression
        self.selection = kwargs.pop("selection", None)
        self.binning = kwargs.pop("binning", (10, 0, 1))
        super(Feature, self).__init__(*args, **kwargs)
        
