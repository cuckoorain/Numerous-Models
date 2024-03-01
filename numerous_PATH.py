class PathProcessor:
    def __init__(self, paths):
        # Assuming paths is a list of functions
        self.paths = paths

    def process(self, path, r1, r2):
        # Apply the first function in the list to the input
        f1 = path[0](r1, r2)
        # Apply the second function in the list to the result of the first function
        f2 = path[1](f1)
        # Return a list containing the results of the two function applications
        return [f1, f2]
