from Palette import Palette
from colour import Color


class DarkPalette(Palette):
    def __init__(self, size):
        super().__init__(size)
        black = Color('#000000')
        white = Color('#FFFFFF')
        self.palette = [c.hex_l for c in black.range_to(white, size // 2)]
        self.palette += [c.hex_l for c in white.range_to(black, size // 2 + 1)][1:]

    def getColor(self, n):
        return self.palette[n]
