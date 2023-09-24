import random
from collections import namedtuple
from typing import NamedTuple


class Direction:
    horizontal = "horizontal"
    vertical = "vertical"


class StatusCell:
    live = "live"
    killed = "killed"


class StatusShip(StatusCell):
    stricken = "stricken"


class Cell:
    count: int
    position: NamedTuple
    status: StatusCell


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp  # 1 - горизонтальная; 2 - вертикальная
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1 for _ in range(length)]

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        """Перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку;
        go = -1 - движение в другую сторону на одну клетку);
        движение возможно только если флаг _is_move = True;"""
        x, y = self.get_start_coords()
        match self._tp:
            case 1:
                x += go
            case 2:
                y += go
        self.set_start_coords(x, y)

    def is_collide(self, ship):
        """Проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с
        текущим или просто соприкасается, в том числе и по диагонали);
        метод возвращает
        True, если столкновение есть и
        False - в противном случае;"""

        def get_all_coords_ship(_ship: Ship):
            _x, _y = _ship.get_start_coords()
            _length = _ship._length
            _coords = []
            for i in range(_length):
                if _ship._tp == 1:
                    _coords.append((_x + i, _y))
                if _ship._tp == 2:
                    _coords.append((_x, _y + i))
            return _coords

        def coord_env(x, y):
            res = []
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    res.append((x + dx, y + dy))
            return res

        coords_self = get_all_coords_ship(self)
        coords_ship = get_all_coords_ship(ship)

        self_ship_env = []
        for coord in coords_self:
            self_ship_env.extend(coord_env(*coord))
        self_ship_env = set(self_ship_env)
        return any(coord in self_ship_env for coord in coords_ship)

    def is_out_pole(self, size=10):
        """Проверка на выход корабля за пределы игрового поля
        (size - размер игрового поля, обычно, size = 10);
        возвращается:
        True, если корабль вышел из игрового поля,
        False - в противном случае."""
        x, y = self.get_start_coords()
        if self._tp == 1:
            return all((0 <= x <= size, 0 <= x + self._length <= size, 0 <= y <= size))
        if self._tp == 2:
            return all((0 <= y <= size, 0 <= y + self._length <= size, 0 <= x <= size))

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


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


if __name__ == "__main__":
    game()
