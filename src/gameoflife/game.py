from grid import Grid
from starters import Starters

configuration = {
    'background': [25, 25, 25],
    'width': 1000,
    'height': 1000,
    'x_cell_number': 50,
    'y_cell_number': 50
}

grid = Grid(configuration)
Starters().stick(grid.game_state)
Starters().automata(grid.game_state)

grid.run()
