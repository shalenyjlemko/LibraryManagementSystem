
class Location:
    def __init__(self, beam: int, shelf: int, level: int):
        self.beam = beam
        self.shelf = shelf
        self.level = level

    def __repr__(self):
        return f"Location(beam={self.beam}, shelf={self.shelf}, level={self.level})"
