class Cell:
    """A 'Cell' is an object within a 'Maze' object.

    A Cell starts with having all walls and is not visited by a 'Player'.
    Credit to Christian Hill: https://scipython.com/blog/making-a-maze/

    Attributes:
        x (int): X co-ordinate of the Cell.
        y (int): Y co-ordinate of the Cell.
        player_trail (bool): True or False if a Player has been to the Cell.
        walls (dict): True or False for each wall in the Cell.

    """

    # fmt: off
    wall_pairs = {
        "N": "S", 
        "E": "W", 
        "W": "E", 
        "S": "N"
    }
    # fmt: on

    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.player_trail = False
        self.walls = {"N": True, "E": True, "W": True, "S": True}

    def check_all_walls(self) -> bool:
        """Return True if the Cell has all walls, otherwise False."""
        return all(self.walls.values())

    def remove_wall(self, other_cell: "Cell", wall: str):
        """Removes a wall between the Cell and another Cell.

        The wall of the Cell will become False and wall on the other Cell will
        be made False by finding the wall's pair with the wall_pairs dictionary.

        Args:
            other_cell (Cell): Another Cell object.
            wall (str): Direction of wall to remove.

        """
        self.walls[wall] = False
        other_cell.walls[Cell.wall_pairs[wall]] = False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def player_trail(self):
        return self._player_trail

    @player_trail.setter
    def player_trail(self, bool):
        self._player_trail = bool

    @property
    def walls(self):
        return self._walls

    @walls.setter
    def walls(self, walls):
        self._walls = walls
