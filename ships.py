import random


class Direction:
    horizontal = 'horizontal'
    vertical = 'vertical'


class StatusCell:
    live = 'live'
    die = 'die'


class StatusShip(StatusCell):
    stricken = 'stricken'


class Cell:
    count: int
    position: tuple
    status: StatusCell


class Ship:
    length: int
    position: tuple
    direction: Direction
    status: StatusShip


class Player:
    def __init__(self, name):
        self.name = name
        self.available_ships = []
        self.ships = []

    def add_ship(self, size, position):
        pass

    def remove_ship(self, size, position):
        pass

    def draw_ships(self):
        pass


class Field:
    pass


def game():
    pass


if __name__ == '__main__':
    game()
