from maze import Maze
from cell import Cell


class Player:
    """A 'Player' can move through a Maze object by showing which Cell objects it has visited.

    A Player starts at (0, 0) in the Maze.

    Attributes:
        current_x (int): Current X co-ordinate of the Player in the Maze.
        current_y (int): Current y co-ordinate of the Player in the Maze.
        delta_coords (list): List of direction and co-ordinate changes.

    """

    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        # fmt: off
        self.delta_coords = [
            ("N", (0, -1)), 
            ("E", (1, 0)), 
            ("W", (-1, 0)), 
            ("S", (0, 1))
        ]
        # fmt: on

    def move(self, maze: "Maze", move_direction: str):
        """Moves the Player in a direction in the Maze.

        If the Player is at the start (0,0), the current Cell's player_trail will become True,
        then it will check if the direction will lead to a valid Cell in the Maze.
        If the Player has been to the valid cell, the current Cell's player_trail becomes False
        and the Player's co-ordinates will be updated.
        If the Player has not been to the valid Cell, the new Cell's player_trail becomes True.

        Args:
            maze (Maze): A Maze object for the Player to move in.
            move_direction (str): The direction of where the Player wants to move.

        """
        current_cell = maze.cell_at(self.current_x, self.current_y)

        if current_cell.x == 0 and current_cell.y == 0:
            current_cell.player_trail = True

        delta_x, delta_y = dict(self.delta_coords)[move_direction]
        new_x = current_cell.x + delta_x
        new_y = current_cell.y + delta_y
        if (0 <= new_x < maze.columns) and (0 <= new_y < maze.rows):
            new_cell = maze.cell_at(new_x, new_y)
            if new_cell.player_trail == True:
                current_cell.player_trail = False
            else:
                new_cell.player_trail = True

            self.current_x = new_x
            self.current_y = new_y

    def find_neighbours(self, maze: "Maze", cell: "Cell") -> list[tuple[str, "Cell"]]:
        """
        TODO
        """
        neighbours = []
        for direction, (delta_x, delta_y) in self.delta_coords:
            new_x = cell.x + delta_x
            new_y = cell.y + delta_y
            if (0 <= new_x < maze.rows) and (0 <= new_y < maze.columns):
                neighbour = maze.cell_at(new_x, new_y)
                if (
                    (direction == "E" and neighbour.walls["W"] == False)
                    or (direction == "S" and neighbour.walls["N"] == False)
                    or (direction == "W" and neighbour.walls["E"] == False)
                    or (direction == "N" and neighbour.walls["S"] == False)
                ):
                    neighbours.append((direction, neighbour))
        return neighbours

    @property
    def current_x(self):
        return self._current_x

    @current_x.setter
    def current_x(self, x):
        self._current_x = x

    @property
    def current_y(self):
        return self._current_y

    @current_y.setter
    def current_y(self, y):
        self._current_y = y

    @property
    def delta_coords(self):
        return self._delta_coords

    @delta_coords.setter
    def delta_coords(self, delta_coords):
        self._delta_coords = delta_coords
