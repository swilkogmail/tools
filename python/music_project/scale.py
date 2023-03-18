class Scale:
    """
    Scale is a name for a series of musical notes
    """

    def __init__(self, key, name, type):
        self.key = key
        self.name = name
        self.type = type


    def description(self):
        return f"{self.key} {self.name} is a {self.type} {self.__class__.__name__}"
    
    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"
