from Fractal import Fractal


class Phoenix(Fractal):
    def __init__(self, max_iterations=100):
        super().__init__(max_iterations)

    def count(self, complex_number):
        """
        Return iteration count of the Phoenix set for a point 'z'
        """
        c = complex(0.5667, 0.0)
        phoenix = complex(-0.5, 0.0)
        zFlipped = complex(complex_number.imag, complex_number.real)
        zPrev = 0 + 0j
        z = zFlipped
        for i in range(self.max_iterations):
            zSave = z
            z = z * z + c + (phoenix * zPrev)
            zPrev = zSave
            if abs(z) > 2.0:
                return i
        return self.max_iterations - 1
