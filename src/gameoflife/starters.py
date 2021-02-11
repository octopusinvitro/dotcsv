from grid import Grid


class Starters:
    def stick(self, grid):
        grid[5, 3] = Grid.ALIVE
        grid[5, 4] = Grid.ALIVE
        grid[5, 5] = Grid.ALIVE

    def automata(self, grid):
        grid[20, 23] = Grid.ALIVE
        grid[21, 21] = Grid.ALIVE
        grid[21, 23] = Grid.ALIVE
        grid[22, 22] = Grid.ALIVE
        grid[22, 23] = Grid.ALIVE
