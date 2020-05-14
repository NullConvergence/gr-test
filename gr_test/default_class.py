class Default(object):
    def __init__(self, name=None):
        print("initialized default class")
        if name is not None:
            self.name = name
        else:
            self.name = "default_name"

        print("Extra line added in commit.")

    def get_name(self):
        if self.name:
            return self.name
        else:
            raise NotImplementedError("Class name not initialized")
