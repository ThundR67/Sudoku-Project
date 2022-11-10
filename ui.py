"""Module to handle the user interface."""
import pygame


class UI:
    """Class to handle the user interface."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")

        self.screen = pygame.display.set_mode((800, 1000))

        self.font = pygame.font.SysFont("monospace", 16)
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

    def main(self):
        """Main loop."""
        self.handle_events()

        self.set_background_image("background.jpg")

        self.clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    ui = UI()
    while True:
        ui.main()