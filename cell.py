import pygame

class Cell:
    sketched_value = 0
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self,value):
        self.value = value

    def get_cell_value(self):
        return self.value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def get_sketched_value(self):
        return self.sketched_value
=======
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self,value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        pass