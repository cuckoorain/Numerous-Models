import numpy as np
class PathProcessor:
    def __init__(self, paths):
        # Assuming paths is a list of functions
        self.paths = paths
        self.ModelsA = Models(self.paths[0])
        self.ModelsB = Models(self.paths[1])
            

    def process(self, r1, r2):
        ret = []
        f1 = self.ModelsA.process_var2(r1,r2)
        f2 = []
        for i in range(len(f1)):
            f2.append(self.ModelsB.process_var1(f1[i]))

        return f2


class Models:
    def __init__(self, models):
        self.models = models
    def process_var2(self, r1, r2):
        res = []
        for model in self.models:
            res.append(model(r1,r2))
        return res
    def process_var1(self, r1):
        res = []
        for model in self.models:
            res.append(model(r1).tolist()[0])
        return res