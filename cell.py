import pygame

class Cell:
    sketched_value = 0
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self,value):
        """Sets the confirmed value of the cell"""
        self.value = value

    def get_cell_value(self):
        """Gets the confirmed value of the cell"""
        return self.value

    def set_sketched_value(self, value):
        """Sets the sketched value of the cell"""
        self.sketched_value = value

    def get_sketched_value(self):
        """Gets the sketched value of the cell"""
        return self.sketched_value