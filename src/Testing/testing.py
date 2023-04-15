import unittest
from Fractal import Fractal
from Phoenix import Phoenix
from Mandelbrot import Mandelbrot
from FractalParser import get_frac_dic
from FractalFactory import make_fractal
from PaletteFactory import makePalette


class Testing(unittest.TestCase):
    def test_get_frac_dic_of_phoenix(self):
        fractal_info = get_frac_dic('../data/phoenix.frac')
        self.assertEqual(0.5667, fractal_info.get('creal'))
        self.assertEqual(0.0, fractal_info.get('cimag'))
        self.assertEqual(3.25, fractal_info.get('axislength'))
        self.assertEqual(512, fractal_info.get('pixels'))

    def test_get_frac_dic_of_julia(self):
        fractal_info = get_frac_dic('../data/julia.frac')
        self.assertEqual(-1.0125, fractal_info.get('creal'))
        self.assertEqual(0.275, fractal_info.get('cimag'))
        self.assertEqual(4.0, fractal_info.get('axislength'))
        self.assertEqual(1024, fractal_info.get('pixels'))

    def test_get_frac_dic_of_mandelbrot3(self):
        fractal_info = get_frac_dic('../data/mandel-pow3.frac')
        self.assertEqual("mandelbrot3", fractal_info.get('type'))
        self.assertEqual(640, fractal_info.get('pixels'))
        self.assertEqual(4.0, fractal_info.get('axislength'))
        self.assertEqual(100, fractal_info.get('iterations'))

    def test_minxy_maxxy(self):
        fractal_info = get_frac_dic('../data/oriental-dragons.frac')
        self.assertEqual(-0.611292072047808 - .5 * 0.0097572606582521, fractal_info.get('min').get('x'))
        self.assertEqual(-0.611292072047808 + .5 * 0.0097572606582521, fractal_info.get('max').get('x'))
        self.assertEqual(-0.0428352613957943 - .5 * 0.0097572606582521, fractal_info.get('min').get('y'))
        self.assertEqual(-0.0428352613957943 + .5 * 0.0097572606582521, fractal_info.get('max').get('y'))

    def test_pixel_size(self):
        fractal_info = get_frac_dic('../data/spiral0.frac')
        fractal_info2 = get_frac_dic('../data/shrimp-cocktail.frac')
        self.assertEqual(0.00497817993164062 / 640, fractal_info.get('pixelsize'))
        self.assertEqual(0.221204819277108 / 512, fractal_info2.get('pixelsize'))

    def test_duck_typing(self):
        fractal_info = get_frac_dic('../data/phoenix.frac')
        fractal = make_fractal(fractal_info)
        self.assertIsInstance(fractal, Fractal)
        self.assertIsInstance(fractal, Phoenix)

        fractal_info = get_frac_dic('../data/spiral0.frac')
        fractal2 = make_fractal(fractal_info)
        self.assertIsInstance(fractal2, Fractal)
        self.assertIsInstance(fractal2, Mandelbrot)

    def test_count(self):
        fractal_info = get_frac_dic('../data/julia.frac')
        fractal = make_fractal(fractal_info)
        self.assertEqual(512, fractal.count(complex(-1.0125, 0.275)))
        self.assertEqual(34, fractal.count(complex(-1, 0)))

    def test_palette_creation(self):
        test_palette = makePalette("DarkPalette", 64)
        self.assertEqual(64, len(test_palette.palette))
        test_palette2 = makePalette("DarkPalette", 512)
        self.assertEqual(512, len(test_palette2.palette))

        test_palette = makePalette("ColorfulPalette", 99)
        self.assertEqual(99, len(test_palette.palette))
        test_palette2 = makePalette("ColorfulPalette", 103)
        self.assertEqual(103, len(test_palette2.palette))


if __name__ == '__main__':
    unittest.main()
