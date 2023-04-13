class Fractal:
    def __init__(self, max_iterations=100):
        self.max_iterations = max_iterations

    def count(self, complex_number):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
