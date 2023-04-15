from Palette import Palette
from colour import Color


class ColorfulPalette(Palette):
    def __init__(self, size):
        super().__init__(size)

        split_size = size // 16 + 1
        extras = size % 16

        red = Color('red')
        yel = Color('yellow')
        grn = Color('green')
        cya = Color('cyan')
        blu = Color('blue')
        mag = Color('magenta')
        blk = Color('black')

        self.palette = [c.hex_l for c in blk.range_to(yel, split_size)]
        self.palette += [c.hex_l for c in yel.range_to(mag, split_size)][1:]
        self.palette += [c.hex_l for c in blk.range_to(grn, split_size)][1:]
        self.palette += [c.hex_l for c in grn.range_to(blk, split_size)][1:]
        self.palette += [c.hex_l for c in blk.range_to(yel, split_size)][1:]
        self.palette += [c.hex_l for c in blu.range_to(red, split_size)][1:]
        self.palette += [c.hex_l for c in blk.range_to(cya, split_size)][1:]
        self.palette += [c.hex_l for c in cya.range_to(blk, split_size)][1:]
        self.palette += [c.hex_l for c in blk.range_to(yel, split_size)][1:]
        self.palette += [c.hex_l for c in yel.range_to(mag, split_size)][1:]
        self.palette += [c.hex_l for c in blk.range_to(grn, split_size)][1:]
        self.palette += [c.hex_l for c in grn.range_to(red, split_size)][1:]
        self.palette += [c.hex_l for c in red.range_to(yel, split_size)][1:]
        self.palette += [c.hex_l for c in blu.range_to(red, split_size)][1:]
        self.palette += [c.hex_l for c in blk.range_to(cya, split_size)][1:]
        self.palette += [c.hex_l for c in cya.range_to(grn, split_size)][1:]
        if extras != 0:
            self.palette += [c.hex_l for c in grn.range_to(yel, extras)][1:]

    def getColor(self, n):
        return self.palette[n]
