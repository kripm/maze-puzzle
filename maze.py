import random

from cell import Cell


class Maze:
    """A 'Maze' made from 'Cell' objects as a grid.

    Credit to Christian Hill: https://scipython.com/blog/making-a-maze/

    Attributes:
        rows (int): Number of rows in the Maze.
        columns (int): Number of columns in the Maze.
        start_x (int): Starting X co-ordinate for initial construction.
        start_y (int): Starting Y co-ordinate for initial construction.

    """

    def __init__(self, rows: int, columns: int):
        self.rows, self.columns = rows, columns
        self.start_x, self.start_y = 1, 1
        self.maze = [
            [Cell(x, y) for y in range(self.columns)] for x in range(self.rows)
        ]

    def make_maze(self):
        """Creates a perfect maze using the depth-first search algorithm.

        Looks at the neighbouring cells. If they are not yet visited, one is
        randomly picked and the wall between them is removed.
        If there are no more unvisited neighbouring cells, it will backtack
        to the last cell with an unvisited neighbour.

        """
        total_cells = self.rows * self.columns
        cell_stack = []
        current_cell = self.cell_at(self.start_x, self.start_y)
        visited_cells = 1

        while visited_cells < total_cells:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                current_cell = cell_stack.pop()
                continue

            direction, next_cell = random.choice(neighbours)
            current_cell.remove_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            visited_cells += 1

    def cell_at(self, x: int, y: int) -> "Cell":
        """Returns the Cell at a given co-ordinate."""
        return self.maze[x][y]

    def find_valid_neighbours(self, cell: "Cell") -> list[tuple[str, "Cell"]]:
        """Returns a list of a Cell's unvisited neighbours.

        Args:
            cell (Cell): A Cell object.

        """
        # fmt: off
        delta_coords = [
            ("N", (0, -1)), 
            ("E", (1, 0)), 
            ("W", (-1, 0)), 
            ("S", (0, 1))
        ]
        # fmt: on
        neighbours = []
        for direction, (delta_x, delta_y) in delta_coords:
            new_x = cell.x + delta_x
            new_y = cell.y + delta_y
            if (0 <= new_x < self.rows) and (0 <= new_y < self.columns):
                neighbour = self.cell_at(new_x, new_y)
                if neighbour.check_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def __str__(self):
        """Returns a really bad text-based interpretation of the maze."""
        maze_rows = ["-" * self.rows * 2]
        for y in range(self.columns):
            maze_row = ["|"]
            for x in range(self.rows):
                if self.maze[x][y].walls["E"]:
                    maze_row.append(" |")
                elif self.maze[x][y].player_trail == True:
                    maze_row.append('🍪')
                else:
                    maze_row.append("  ")
            maze_rows.append("".join(maze_row))
            maze_row = ["|"]
            for x in range(self.columns):
                if self.maze[x][y].walls["S"]:
                    maze_row.append("-+")
                elif self.maze[x][y].player_trail == True:
                    maze_row.append('🍪')
                else:
                    maze_row.append(" +")
            maze_rows.append("".join(maze_row))
        return "\n".join(maze_rows)

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self._rows = rows

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, columns):
        self._columns = columns
