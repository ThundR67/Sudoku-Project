"""Module to handle the user interface."""
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
LIGHT_ORANGE = (255, 200, 0)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREY = (128, 128, 128)

class UI:
    """Class to handle the user interface."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")

        self.screen = pygame.display.set_mode((800, 1000))
        self.clock = pygame.time.Clock()

    def handle_events(self):
        """Handles all the events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def set_background_image(self, image_location):
        """Sets the background image."""
        image = pygame.image.load(image_location)
        self.screen.blit(image, (0, 0))

    def show_text(self, text, size, color, position, bold=False):
        """Shows text on the screen."""
        font = pygame.font.SysFont("monospace", size, bold=bold)
        label = font.render(text, True, color)
        self.screen.blit(label, position)

    def show_button(self, text, coordinates, size):
        """Shows a button on the screen."""
        mouse = pygame.mouse.get_pos()

        is_mouse_in_x = coordinates[0] < mouse[0] < coordinates[0] + size[0]
        is_mouse_in_y = coordinates[1] < mouse[1] < coordinates[1] + size[1]

        color = LIGHT_ORANGE if is_mouse_in_x and is_mouse_in_y else ORANGE

        pygame.draw.rect(self.screen, color, (coordinates[0], coordinates[1], size[0], size[1]))

        font = pygame.font.SysFont("monospace", 50, bold=True)
        label = font.render(text, True, WHITE)

        self.screen.blit(label, (coordinates[0] + (size[0] - label.get_width()) / 2, coordinates[1] + (size[1] - label.get_height()) / 2))

    def main(self):
        """Main loop."""
        self.handle_events()

        self.set_background_image("background.jpg")

        self.show_text("Welcome to Sudoku", 70, BLACK, (45, 50), bold=True)

        self.show_text("Select Game Mode:", 50, BLACK, (160, 600), bold=True)

        self.show_button("Easy", (50, 700), (200, 100))
        self.show_button("Medium", (300, 700), (200, 100))
        self.show_button("Hard", (550, 700), (200, 100))

        self.clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    ui = UI()
    while True:
        ui.main()