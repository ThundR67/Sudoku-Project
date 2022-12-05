import pygame
from sudoku_generator import SudokuGenerator
from cell import Cell
class Board:
    selected_cell = [0,0]
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.generated_board = SudokuGenerator(9,difficulty)
        self.generated_board.fill_values()
        self.solved_board = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.generated_board.get_board()[i][j]
                self.solved_board[i][j] = value

        self.generated_board.remove_cells()

        self.cell_array = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                value = self.generated_board.get_board()[i][j]
                self.cell_array[i][j] = Cell(value,i,j,self.screen)


    def draw(self):
        font = pygame.font.SysFont("monospace", 40, bold=True)
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(self.screen,(0,0,0),pygame.Rect(j*70+85,i*70+5,70,70),1)
                if self.cell_array[i][j].get_cell_value() != 0:
                    label = font.render(str(self.cell_array[i][j].get_cell_value()), True, (0,0,0))
                    self.screen.blit(label, (j*70+104,i*70+20))
                else:
                    if self.cell_array[i][j].get_sketched_value() != 0:
                        label = font.render(str(self.cell_array[i][j].get_sketched_value()), True, (128,128,128))
                        self.screen.blit(label, (j * 70 + 104, i * 70 + 20))


        pygame.draw.rect(self.screen,(0,0,0),pygame.Rect(85,5,630,630),4)
        pygame.draw.line(self.screen,(0,0,0),(295,5),(295,634),4)
        pygame.draw.line(self.screen, (0, 0, 0), (505, 5), (505, 634), 4)
        pygame.draw.line(self.screen, (0, 0, 0), (85, 215), (714, 215), 4)
        pygame.draw.line(self.screen, (0, 0, 0), (85, 425), (714, 425), 4)

        pygame.draw.rect(self.screen, (255, 0, 0),pygame.Rect(self.selected_cell[1] * 70 + 85, self.selected_cell[0] * 70 + 5, 70, 70), 4)



    def select(self, row, col):
        self.selected_cell = [row,col]

    def get_selected(self):
        return self.selected_cell

    def select_move(self, direction):
        if direction == "UP" and self.selected_cell[0] !=0:
            self.selected_cell[0] -=1
        elif direction == "DOWN" and self.selected_cell[0] !=8:
            self.selected_cell[0] +=1
        elif direction == "LEFT" and self.selected_cell[1] !=0:
            self.selected_cell[1] -=1
        elif direction == "RIGHT" and self.selected_cell[1] !=8:
            self.selected_cell[1] +=1



    def click(self, x, y):
        pass

    def clear(self):
        if self.cell_array[self.selected_cell[0]][self.selected_cell[1]].get_cell_value() == self.cell_array[self.selected_cell[0]][self.selected_cell[1]].get_sketched_value():
            self.cell_array[self.selected_cell[0]][self.selected_cell[1]].set_cell_value(0)
            self.cell_array[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(0)
        elif self.cell_array[self.selected_cell[0]][self.selected_cell[1]].get_cell_value() == 0:
            self.cell_array[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(0)

    def sketch(self, value):
        if self.cell_array[self.selected_cell[0]][self.selected_cell[1]].get_cell_value() == 0:
            self.cell_array[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(value)

    def place_number(self):
        value = self.cell_array[self.selected_cell[0]][self.selected_cell[1]].get_sketched_value()
        if self.cell_array[self.selected_cell[0]][self.selected_cell[1]].get_cell_value() == 0:
            self.cell_array[self.selected_cell[0]][self.selected_cell[1]].set_cell_value(value)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.cell_array[i][j].get_sketched_value() != 0:
                    self.cell_array[i][j].set_cell_value(0)

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cell_array[i][j].get_cell_value() == 0:
                    return True
        return False

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self.cell_array[i][j].get_cell_value() != self.solved_board[i][j]:
                    return False
        return True