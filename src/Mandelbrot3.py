from Fractal import Fractal


class Mandelbrot3(Fractal):
    def __init__(self, max_iterations):
        super().__init__(max_iterations)

    def count(self, complex_number):
        """
        Return iteration count of the Mandelbrot^3 set for a point at the complex_number
        """
        z = complex(0, 0)  # z0
        for i in range(self.max_iterations):
            z = z * z * z + complex_number  # Get z1, z2, ...
            if abs(z) > 2.0:
                return i
        return self.max_iterations - 1
