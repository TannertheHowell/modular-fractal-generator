from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, max_iterations, creal, cimag):
        super().__init__(max_iterations)
        self.c = complex(creal, cimag)

    def count(self, complex_number):
        z = complex_number
        for i in range(self.max_iterations):
            if abs(z) > 2:
                return i
            z = z * z + self.c
        return self.max_iterations
