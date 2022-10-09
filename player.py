from maze import Maze


class Player:
    """A 'Player' can move through a Maze object by showing which Cell objects it has visited.
    
    A Player starts at (0, 0) in the Maze.
    
    Attributes:
        id (int): An identification number for the Player object.
        current_x (int): Current X co-ordinate of the Player in the Maze.
        current_y (int): Current y co-ordinate of the Player in the Maze.
    
    """
    
    def __init__(self, id: int):
        self.id = id
        self.current_x = 0
        self.current_y = 0
        
    def move(self, maze: 'Maze', move_direction: str):
        """Moves the Player in a direction in the Maze.
        
        If the Player is at the start (0,0), the current Cell's player_trail will become True,
        then it will check if the direction will lead to a valid Cell in the Maze.
        If the Cell is valid, the Player's co-ordinates will be updated and 
        the Cell's player_trail will become True to show that the Player has been to that cell.
        
        Args:
            maze (Maze): A Maze object for the Player to move in.
            move_direction (str): The direction of where the Player wants to move.
        
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
