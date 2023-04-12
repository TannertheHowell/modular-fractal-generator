class Fractal:
    def __init__(self, max_iteration=100):
        self.max_iteration = max_iteration

    def count(self, complex_number):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
