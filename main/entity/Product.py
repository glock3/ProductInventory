class Product:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        string = ' pid: {self.id}, name: {self.name}, description: {self.description} '.format(self=self)
        return string

    def __eq__(self, other):
        is_equal = (self.id == other.id) and (self.name == other.name) and (self.description == other.description)
        return is_equal