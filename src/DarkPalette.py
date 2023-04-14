from Palette import Palette
from colour import Color


class DarkPalette(Palette):
    def __init__(self, size):
        super().__init__(size)
        start = Color('#000000')
        self.palette = [c.hex_l for c in start.range_to('#FFFFFF', size)]

    def getColor(self, n):
        return self.palette[n]
