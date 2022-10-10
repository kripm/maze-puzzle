from maze import Maze
from player import Player


class Solver(Player):
    """
    TODO
    """

    def solve(self, maze: "Maze") -> bool:
        """
        TODO
        """
        cell_stack = []
        visited_cells = []
        current_cell = maze.cell_at(self.current_x, self.current_y)

        while True:
            neighbours = [
                neighbour
                for neighbour in self.find_neighbours(maze, current_cell)
                if neighbour[1] not in visited_cells
            ]

            if (current_cell.x == (maze.columns - 1)) and (
                current_cell.y == (maze.rows - 1)
            ):
                return True
            elif not neighbours:
                visited_cells.append(current_cell)
                current_cell.player_trail = False
                current_cell = cell_stack.pop()
                self.current_x, self.current_y = current_cell.x, current_cell.y
                continue

            possible_directions = []
            possible_cells = []
            for neighbour in neighbours:
                possible_directions.append(neighbour[0])
                possible_cells.append(neighbour[1])
            cell_stack.append(current_cell)

            for direction in ["E", "S", "W", "N"]:
                if direction in possible_directions:
                    self.move(maze, direction)
                    visited_cells.append(current_cell)
                    current_cell = possible_cells[possible_directions.index(direction)]
                    break
