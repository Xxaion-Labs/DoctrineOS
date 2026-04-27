class Doctrine:
    def __init__(self, name, definition=None, id=None):
        self.name = name
        self.definition = definition
        self.id = id

    def mount(self):
        print(f"[doctrine] mounted: {self.name}")
