import pytest
from qbe_factor.models import (
    CountryCategory,
    AgeGroupCategory,
    FactorModel,
    Variable,
    VariableFactor,
)
from pydantic import ValidationError
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


def test_variable():
    # happy path for country
    vf = Variable(var_name="country", category="UK")
    assert vf.var_name.value == "country"
    assert vf.category.value == "UK"
    assert isinstance(vf.category, CountryCategory)

    # happy path for age_group
    vf = Variable(var_name="age_group", category="50+")
    assert vf.var_name.value == "age_group"
    assert vf.category.value == "50+"
    assert isinstance(vf.category, AgeGroupCategory)
    assert vf.category == AgeGroupCategory.AGE_50_PLUS
    assert vf.category.value == "50+"

    # completely invalid var_name (caught by default pydantic checking)
    with pytest.raises(ValidationError):
        vf = Variable(var_name="bad", category="UK")

    # completely invalid category (caught by default pydantic checking)
    with pytest.raises(ValidationError):
        vf = Variable(var_name="country", category="bad")

    # Age group category passed for country variable (custom model validation)
    with pytest.raises(ValidationError) as exception:
        vf = Variable(var_name="country", category="50+")
    error_message = repr(exception.value.errors())
    assert "Invalid category" in error_message, "custom error message"
    assert "var_name 'country'" in error_message, "contains the var_name"
    assert "Australia" in error_message, "contains the valid values."

    # Country category passed for age_group variable (custom model validation)
    with pytest.raises(ValidationError) as exception:
        vf = Variable(var_name="age_group", category="UK")
    error_message = repr(exception.value.errors())
    assert "Invalid category" in error_message, "custom error message"
    assert "var_name 'age_group'" in error_message, "contains the var_name"
    assert "18-30" in error_message, "contains the valid values."


def test_variable_factor():
    # happy path for country
    vf = VariableFactor(var_name="country", category="UK", factor=0.5)
    assert vf.var_name.value == "country"
    assert vf.category.value == "UK"
    assert isinstance(vf.category, CountryCategory)
    assert vf.factor == 0.5

    # happy path for age_group
    vf = VariableFactor(var_name="age_group", category="50+", factor=0.6)
    assert vf.var_name.value == "age_group"
    assert vf.category.value == "50+"
    assert isinstance(vf.category, AgeGroupCategory)
    assert vf.category == AgeGroupCategory.AGE_50_PLUS
    assert vf.category.value == "50+"
    assert vf.factor == 0.6

    # completely invalid var_name (caught by default pydantic checking)
    with pytest.raises(ValidationError):
        vf = VariableFactor(var_name="bad", category="UK", factor=0.5)

    # completely invalid category (caught by default pydantic checking)
    with pytest.raises(ValidationError):
        vf = VariableFactor(var_name="country", category="bad", factor=0.5)

    # Age group category passed for country variable (custom model validation)
    with pytest.raises(ValidationError) as exception:
        vf = VariableFactor(var_name="country", category="50+", factor=0.5)
    error_message = repr(exception.value.errors())
    assert "Invalid category" in error_message, "custom error message"
    assert "var_name 'country'" in error_message, "contains the var_name"
    assert "Australia" in error_message, "contains the valid values."

    # Country category passed for age_group variable (custom model validation)
    with pytest.raises(ValidationError) as exception:
        vf = VariableFactor(var_name="age_group", category="UK", factor=0.5)
    error_message = repr(exception.value.errors())
    assert "Invalid category" in error_message, "custom error message"
    assert "var_name 'age_group'" in error_message, "contains the var_name"
    assert "18-30" in error_message, "contains the valid values."


def test_get_factor():
    model = FactorModel.load()
    assert model.get_factor("country", "UK") == 0.25
    assert model.get_factor("age_group", "50+") == 0.34

    with pytest.raises(ValueError):
        model.get_factor("missing", "missing")

    with pytest.raises(ValueError):
        model.get_factor("country", "18-30")


def test_get_factors():
    model = FactorModel.load()
    input_data = load_json_file("tests/example_input.json")
    variables = input_data["data"]
    variable_factors = model.get_factors(variables)

    for variable, variable_factor in zip(variables, variable_factors):
        assert isinstance(variable_factor, VariableFactor)
        assert variable["var_name"] == variable_factor.var_name.value
        assert variable["category"] == variable_factor.category.value

        assert isinstance(variable_factor.factor, float)
        assert 0.0 <= variable_factor.factor <= 1.0  # Python chained comparison
