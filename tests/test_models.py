import pytest
from qbe_factor.models import FactorModel


def test_load_filename():
    model = FactorModel.load("tests/test_data.json")
    data = model.data["data"]
    for i in range(2):
        assert data[i]["var_name"] == "variable"
        assert data[i]["category"] == f"value{i}"


def test_load_default():
    model = FactorModel.load()
    data = model.data["data"]
    for i in range(len(data)):
        assert "var_name" in data[i]
        assert "category" in data[i]
