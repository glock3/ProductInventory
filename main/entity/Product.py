class Product:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        string = ' pid: {self.id}, name: {self.name}, description: {self.description} '.format(self=self)
        return string
