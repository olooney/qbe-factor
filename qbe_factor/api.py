from fastapi import FastAPI, HTTPException
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
    # All validation occurs as pydantic checks the POSTed JSON against
    # the VariableList schema, including the category/var_name mismatch.
    # If any errors are found it will throw a ValidationError which will
    # return a 422 HTTP response. If we reach this line of code, we know
    # that all input was in fact valid.
    return {"valid": True, "message": "All variables are valid."}


@app.post("/get_factors")
async def get_factors(variable_list: VariableList) -> FactorResults:
    try:
        variables = variable_list.data
        factors = list(model.get_factors(variables))
        return { "results": factors }
    except ValueError as ex:
        raise HTTPException(status_code=500, detail=ex.args[0])
