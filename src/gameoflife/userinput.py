import numpy


class UserInput:
    def __init__(self, x_cell_number, y_cell_number):
        self.x_cell_number = x_cell_number
        self.y_cell_number = y_cell_number
        self.play = True

    def update_state(self, pygame, updatable_game_state):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                self.play = not self.play

            # mouse_click = pygame.mouse.get_pressed()
            # if sum(mouse_click) > 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posX, posY = pygame.mouse.get_pos()
                celX, celY = int(numpy.floor(posX / self.x_cell_number)), int(numpy.floor(posY / self.y_cell_number))
                updatable_game_state[celX, celY] = Grid.ALIVE
