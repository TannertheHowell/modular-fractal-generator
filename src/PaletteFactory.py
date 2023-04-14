from DarkPalette import DarkPalette
from ColorfulPalette import ColorfulPalette


def makePalette(palette_name, size):
    if palette_name == 'DarkPalette':
        return DarkPalette(size)
    elif palette_name == 'ColorfulPalette' or palette_name == "":
        return ColorfulPalette(size)
    else:
        raise NotImplementedError("Invalid palette requested")
