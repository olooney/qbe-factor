from fastapi import FastAPI
import pydantic
from typing import List
from .models import VarName, Variable, VariableFactor, FactorModel


app = FastAPI()
model = FactorModel.load()


class PingResponse(pydantic.BaseModel):
    message: str


class VariableList(pydantic.BaseModel):
    data: List[Variable]


class FactorResults(pydantic.BaseModel):
    results: List[VariableFactor]


class ValidationResults(pydantic.BaseModel):
    valid: bool
    message: str


@app.get("/ping")
async def ping() -> PingResponse:
    return {"message": "PONG"}


@app.post("/validate")
async def validate(variable_list: VariableList) -> ValidationResults:
    variables = variable_list.data
    try:
        model.get_factors(variables)
    except ValueError as ex:
        return {"valid": False, "message": ex.message}

    return {"valid": True, "message": ""}


@app.post("/get_factors")
async def get_factors(variable_list: VariableList) -> FactorResults:
    variables = variable_list.data
    factors = list(model.get_factors(variables))
    return {"results": factors}
