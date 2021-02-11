class Display:
    def __init__(self, pygame, configuration):
        height = configuration['height']
        width = configuration['width']

        self.x_size = width / configuration['x_cell_number']
        self.y_size = height / configuration['y_cell_number']
        self.screen = pygame.display.set_mode((height, width))

        self.background = configuration['background']

    def refresh(self):
        self.screen.fill(self.background)

    def draw_dead_cell(self, pygame, x, y):
        pygame.draw.polygon(self.screen, (128, 128, 128), self._polygon(x, y), 1)

    def draw_alive_cell(self, pygame, x, y):
        pygame.draw.polygon(self.screen, (255, 255, 255), self._polygon(x, y), 0)

    def _polygon(self, x, y):
        return [
            ((x)     * self.x_size, (y)     * self.y_size),
            ((x + 1) * self.x_size, (y)     * self.y_size),
            ((x + 1) * self.x_size, (y + 1) * self.y_size),
            ((x)     * self.x_size, (y + 1) * self.y_size)
        ]
