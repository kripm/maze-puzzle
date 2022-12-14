from player import Player


class Human(Player):
    """A 'Human' is a subclass of a Player class with a name and a high score.

    Attributes:
        id (int): An identification number for the Human.
        name (str): The name of the Human.
        high_score (int): The biggest Maze the Human has completed.

    """

    def __init__(self, id: int, name: str, high_score: int = 0):
        self.id = id
        self.name = name
        self.high_score = high_score

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def high_score(self):
        return self._high_score

    @high_score.setter
    def high_score(self, high_score):
        self._high_score = high_score
