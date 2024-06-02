import json
import pkgutil
from typing import Iterable, Dict, Union
from enum import Enum
import pydantic


class VarName(Enum):
    COUNTRY = "country"
    AGE_GROUP = "age_group"


class CountryCategory(Enum):
    UK = "UK"
    AUSTRALIA = "Australia"
    CHINA = "China"
    JAPAN = "Japan"


class AgeGroupCategory(Enum):
    AGE_18_30 = "18-30"
    AGE_30_50 = "30-50"
    AGE_50_PLUS = "50+"


CATEGORY_ENUM_BY_VAR_NAME = {
    VarName.COUNTRY: CountryCategory,
    VarName.AGE_GROUP: AgeGroupCategory,
}


class Variable(pydantic.BaseModel):
    var_name: VarName
    category: Union[CountryCategory, AgeGroupCategory]

    @pydantic.model_validator(mode="after")
    def validate_category_var_name_match(self):
        CategoryEnum = CATEGORY_ENUM_BY_VAR_NAME[self.var_name]
        if not isinstance(self.category, CategoryEnum):
            legal_values = [c.value for c in CategoryEnum]
            raise ValueError(
                f"Invalid category {self.category.value!r} for var_name {self.var_name.value!r}; "
                f"Valid values for {self.var_name.value!r} are {legal_values!r}."
            )
        return self


class VariableFactor(Variable):
    factor: float


class FactorModel:
    """
    Returns risk adjustment factors for various demographic categories.
    """

    def __init__(self, factor_data):
        self.data = factor_data

        # create a quick O(1) lookup table to map the pair (var_name, category)
        # directly to the factor.
        self.index = {}
        for variable in self.data["data"]:
            key = (variable["var_name"], variable["category"])
            self.index[key] = variable["factor"]

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

    def get_factor(self, var_name: VarName, category: Union[str, Enum]) -> float:
        """
        Return the factor for the given category of the given variable.

        Raises a ValueError if the category value is not valid.
        """
        if isinstance(var_name, VarName):
            var_name = var_name.value

        if isinstance(category, Enum):
            category = category.value

        key = (var_name, category)
        factor = self.index.get(key, None)

        if factor is None:
            raise ValueError(
                f"Category {category!r} not valid for variable {var_name!r}."
            )

        return factor

    def get_factors(
        self, variables: Iterable[Union[Variable, Dict]]
    ) -> Iterable[VariableFactor]:
        """
        Processes an interable of variables (var_name/category dicts) and adds
        the factor to each. You can either pass `qbe_factor.models.Variable`
        model, or you can pass dicts with the same keys.

        Raises a ValueError if any is invalid.
        """
        for variable in variables:
            if not isinstance(variable, Variable):
                variable = Variable(**variable)

            factor = self.get_factor(variable.var_name.value, variable.category)

            yield VariableFactor(
                var_name=variable.var_name,
                category=variable.category,
                factor=factor,
            )
