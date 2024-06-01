import json
import pkgutil

data = pkgutil.get_data("hermes", "templates/python.tpl")


class FactorModel:
    """
    Returns risk adjustment factors for various demographic categories

    """

    def __init__(self, factor_data={}):
        self.data = factor_data

    @classmethod
    def load(cls, filename=None):
        """
        Load the model's data from the Python package's data by default,
        or allow the user to specify a different JSON file.
        """
        if filename is None:
            raw_data = pkgutil.get_data("qbe_factor", "data/data.json")
            factor_data = json.loads(raw_data.decode("utf-8"))
        else:
            with open(filename) as file:
                factor_data = json.load(file)

        return cls(factor_data)
