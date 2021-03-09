class BaseObject(object):
    def __init__(self, *args, **kwargs):
        self.aux = kwargs

    def get_aux(self, field, default_value=None):
        if field in self.aux:
            return self.aux[field]
        else:
            return default_value
