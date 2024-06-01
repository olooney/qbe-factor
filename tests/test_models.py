import pytest
from qbe_factor.models import FactorModel, VariableFactor
from .util import load_json_file


def test_load_filename():
    model = FactorModel.load("tests/test_data.json")
    data = model.data["data"]

    for i in range(4):
        assert "var_name" in data[i]
        assert data[i]["var_name"].startswith("variable")

        assert "category" in data[i]
        assert data[i]["category"].startswith("value")

        assert "factor" in data[i]
        assert isinstance(data[i]["factor"], float)


def test_load_default():
    model = FactorModel.load()
    data = model.data["data"]

    for i in range(len(data)):
        assert "var_name" in data[i]
        assert "category" in data[i]
        assert "factor" in data[i]


def test_get_factor():
    model = FactorModel.load()
    assert model.get_factor("country", "UK") == 0.25
    assert model.get_factor("age_group", "50+") == 0.34

    with pytest.raises(ValueError):
        model.get_factor("missing", "missing")


def test_get_factors():
    model = FactorModel.load()
    input_data = load_json_file("tests/test_input.json")
    variables = input_data["data"]
    variable_factors = model.get_factors(variables)

    for variable, variable_factor in zip(variables, variable_factors):
        assert isinstance(variable_factor, VariableFactor)
        assert variable["var_name"] == variable_factor.var_name.value
        assert variable["category"] == variable_factor.category

        assert isinstance(variable_factor.factor, float)
        assert 0.0 <= variable_factor.factor <= 1.0  # Python chained comparison
