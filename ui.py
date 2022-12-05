"""Module to handle the user interface."""
import pygame
from sudoku_board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
LIGHT_ORANGE = (255, 200, 0)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREY = (128, 128, 128)

class UI:
    """Class to handle the user interface."""
    current_screen = "intro"
    difficulty = 0
    mouse_clicked = False
    board = 0
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")

        self.screen = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()


    def handle_events(self):
        """Handles all the events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.board.select_move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.board.select_move("RIGHT")
                elif event.key == pygame.K_UP:
                    self.board.select_move("UP")
                elif event.key == pygame.K_DOWN:
                    self.board.select_move("DOWN")

                if event.key == pygame.K_1:
                    self.board.sketch(1)
                if event.key == pygame.K_2:
                    self.board.sketch(2)
                if event.key == pygame.K_3:
                    self.board.sketch(3)
                if event.key == pygame.K_4:
                    self.board.sketch(4)
                if event.key == pygame.K_5:
                    self.board.sketch(5)
                if event.key == pygame.K_6:
                    self.board.sketch(6)
                if event.key == pygame.K_7:
                    self.board.sketch(7)
                if event.key == pygame.K_8:
                    self.board.sketch(8)
                if event.key == pygame.K_9:
                    self.board.sketch(9)
                if event.key == pygame.K_BACKSPACE:
                    self.board.clear()
                if event.key == pygame.K_RETURN:
                    self.board.place_number()


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
        label = font.render(text.upper(), True, WHITE)

        self.screen.blit(label, (coordinates[0] + (size[0] - label.get_width()) / 2, coordinates[1] + (size[1] - label.get_height()) / 2))

    def button_clicked(self, button_rect):
        mouse = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.mouse_clicked == False:
                self.mouse_clicked = True
                return True

        if pygame.mouse.get_pressed()[0] == 0:
            self.mouse_clicked = False


    def show_intro_screen(self):
        """Shows the intro screen."""
        self.set_background_image("background.jpg")

        self.show_text("Welcome to Sudoku", 70, BLACK, (45, 50), bold=True)
        self.show_text("Select Game Mode:", 50, BLACK, (160, 550), bold=True)

        self.show_button("Easy", (50, 650), (200, 100))
        if self.button_clicked(pygame.Rect(50, 650, 200, 100)):
            self.board = Board(9,9,self.screen,30)
            self.current_screen = "game"

        self.show_button("Medium", (300, 650), (200, 100))
        if self.button_clicked(pygame.Rect(300, 650, 200, 100)):
            self.board = Board(9,9,self.screen,40)
            self.current_screen = "game"

        self.show_button("Hard", (550, 650), (200, 100))
        if self.button_clicked(pygame.Rect(550, 650, 200, 100)):
            self.board = Board(9, 9, self.screen, 50)
            self.current_screen = "game"

    def show_win_screen(self):
        """Shows the win screen."""
        self.set_background_image("background.jpg")

        self.show_text("Game Won!", 100, BLACK, (150, 300), bold=True)

        self.show_button("EXIT", (300, 500), (200, 100))
        if self.button_clicked(pygame.Rect(300, 500, 200, 100)):
            pygame.quit()
            quit()

    def show_lose_screen(self):
        """Shows the lose screen."""
        self.set_background_image("background.jpg")

        self.show_text("Game Over :(", 70, BLACK, (150, 300), bold=True)

        self.show_button("RESTART", (270, 500), (250, 100))
        if self.button_clicked(pygame.Rect(270, 500, 250, 100)):
            self.current_screen = "intro"

    def show_game_in_progress_screen(self):
        self.screen.fill(LIGHT_BLUE)
        self.board.draw()

        for i in range(9):
            for j in range(9):
                if self.button_clicked(pygame.Rect(j*70+85,i*70+5,70,70)):
                    self.board.select(i,j)

        self.show_button("RESET", (50, 650), (200, 100))
        if self.button_clicked(pygame.Rect(50, 650, 200, 100)):
            pass

        self.show_button("RESTART", (290, 650), (220, 100))
        if self.button_clicked(pygame.Rect(300, 650, 200, 100)):
            self.current_screen = "intro"

        self.show_button("EXIT", (550, 650), (200, 100))
        if self.button_clicked(pygame.Rect(550, 650, 200, 100)):
            pygame.quit()
            quit()

        if self.board.find_empty() == False:
            if self.board.check_board():
                self.current_screen = "win"
            else:
                self.current_screen = "lose"


    def screen_switcher(self):
        if self.current_screen == "intro":
            self.show_intro_screen()
        elif self.current_screen == "game":
            self.show_game_in_progress_screen()
        elif self.current_screen == "lose":
            self.show_lose_screen()
        elif self.current_screen == "win":
            self.show_win_screen()
        else:
            self.show_intro_screen()

    def main(self):
        """Main loop."""
        self.handle_events()

        self.screen_switcher()
        self.clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    ui = UI()
    while True:

     