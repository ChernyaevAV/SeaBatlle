import random


class Direction:
    horizontal = 'horizontal'
    vertical = 'vertical'


class StatusCell:
    live = 'live'
    killed = 'killed'


class StatusShip(StatusCell):
    stricken = 'stricken'


class Cell:
    count: int
    position: tuple
    status: StatusCell


class Ship:
    size: int
    position: tuple
    direction: Direction
    status: StatusShip


class Field:
    pass


class Player:
    def __init__(self, name):
        self.name = name
        self.available_ships = []
        self.ships = []

    def add_ship(self, ship: Ship):
        self.ships.append(ship)

    def remove_ship(self, ship: Ship):
        self.ships.remove(ship)

    def draw_ships(self):
        pass


def game():
    pass


if __name__ == '__main__':
    game()
