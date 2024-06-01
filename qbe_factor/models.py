import json

class FactorModel:
    """
    TODO
    """

    def __init__(self, factor_data={}):
        self.data = factor_data

    @classmethod
    def load(cls, filename):
        with open(filename) as file:
            factor_data = json.load(file)
        return cls(factor_data)
        

