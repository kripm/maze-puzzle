from maze import Maze


class Player:
    """ TODO
    
    """
    def __init__(self, id: int):
        self.id = id
        self.current_x = 0
        self.current_y = 0
        
    def move(self, maze: 'Maze', move_direction: str):
        """ TODO
        
        """
        # fmt: off
        delta_coords = [
            ("N", (0, -1)), 
            ("E", (1, 0)), 
            ("W", (-1, 0)), 
            ("S", (0, 1))
        ]
        # fmt: on
        current_cell = maze.cell_at(self.current_x, self.current_y)
        if current_cell.x == 0 and current_cell.y == 0:
            current_cell.player_trail = True
        delta_x, delta_y = dict(delta_coords)[move_direction]
        
        new_x = current_cell.x + delta_x
        new_y = current_cell.y + delta_y
        if (0 <= new_x < maze.columns) and (0 <= new_y < maze.rows):
            maze.cell_at(new_x, new_y).player_trail = True
            self.current_x = new_x
            self.current_y = new_y
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
