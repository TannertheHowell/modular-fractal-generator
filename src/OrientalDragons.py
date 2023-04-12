from Fractal import Fractal
import math


# Found the c value and z equation on a forum :link
class OrientalDragons(Fractal):
    def __init__(self, max_iterations=100, c=0.28 + 0.008j):
        super().__init__(max_iterations)
        self.c = c

    def count(self, complex_number):
        z = complex_number
        for i in range(self.max_iterations):
            if abs(z) > 2:
                return i
            z = complex(math.sin(z.real), math.cos(z.imag)) * z + self.c
        return self.max_iterations
