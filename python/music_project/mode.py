from scale import Scale
class Mode(Scale):
    
    def __init__(self, key, name, type, notes):
        super().__init__(key, name, type)
        self.notes = notes

    def description(self):
        initial = super().description()
        return f"{initial} containing notes {self.notes}"
    
    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"