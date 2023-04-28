import sys


class Cube:
    class Diode:
        def __init__(self):
            self.r: int = 0
            self.g: int = 0
            self.b: int = 0

    def __init__(self):
        self.diodes = list[list[list[Cube.Diode]]]()

    def set_color(self, x, y, z, r, g, b):
        self.diodes[x][y][z].r = r
        self.diodes[x][y][z].g = g
        self.diodes[x][y][z].b = b
