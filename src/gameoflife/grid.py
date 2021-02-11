import pygame
import numpy
import time

from display import Display
from userinput import UserInput


class Grid:
    DEAD = 0
    ALIVE = 1

    def __init__(self, configuration):
        pygame.init()
        self.display = Display(pygame, configuration)
        self.display.refresh()
        pygame.display.update()

        self.x_cell_number = configuration['x_cell_number']
        self.y_cell_number = configuration['y_cell_number']
        self.game_state = numpy.zeros((self.x_cell_number, self.y_cell_number))
        self.user_input = UserInput(self.x_cell_number, self.y_cell_number)

    def run(self):
        updatable_game_state = numpy.copy(self.game_state)

        while True:
            self.display.refresh()
            # pygame.display.update()
            time.sleep(0.1)

            self.user_input.update_state(pygame, updatable_game_state)

            if self.user_input.play:
                self._play(updatable_game_state)

            self.game_state = updatable_game_state

    def _play(self, updatable_game_state):
        for y in range(0, self.x_cell_number):
            for x in range(0, self.y_cell_number):
                neighbours = self._neighbours(x, y)

                if self.game_state[x, y] == self.DEAD and neighbours == 3:
                    updatable_game_state[x, y] = self.ALIVE

                elif self.game_state[x, y] == self.ALIVE and (neighbours < 2 or neighbours > 3):
                    updatable_game_state[x, y] = self.DEAD

                if updatable_game_state[x, y] == self.DEAD:
                    self.display.draw_dead_cell(pygame, x, y)
                else:
                    self.display.draw_alive_cell(pygame, x, y)

        pygame.display.update()

    def _neighbours(self, x, y):
        return 0 + \
            self.game_state[(x - 1) % self.x_cell_number, (y - 1) % self.y_cell_number] + \
            self.game_state[(x)     % self.x_cell_number, (y - 1) % self.y_cell_number] + \
            self.game_state[(x + 1) % self.x_cell_number, (y - 1) % self.y_cell_number] + \
            self.game_state[(x - 1) % self.x_cell_number, (y)     % self.y_cell_number] + \
            self.game_state[(x + 1) % self.x_cell_number, (y)     % self.y_cell_number] + \
            self.game_state[(x - 1) % self.x_cell_number, (y + 1) % self.y_cell_number] + \
            self.game_state[(x)     % self.x_cell_number, (y + 1) % self.y_cell_number] + \
            self.game_state[(x + 1) % self.x_cell_number, (y + 1) % self.y_cell_number]
