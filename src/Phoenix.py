from Fractal import Fractal


class Phoenix(Fractal):
    def __init__(self, max_iterations, creal, cimag, preal, pimag):
        super().__init__(max_iterations)
        self.c = complex(creal, cimag)
        self.p = complex(preal, pimag)

    def count(self, complex_number):
        """
        Return iteration count of the Phoenix set for a point 'z'
        """
        zFlipped = complex(complex_number.imag, complex_number.real)
        zPrev = 0 + 0j
        z = zFlipped
        for i in range(self.max_iterations):
            zSave = z
            z = z * z + self.c + (self.p * zPrev)
            zPrev = zSave
            if abs(z) > 2.0:
                return i
        return self.max_iterations - 1
