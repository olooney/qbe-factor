from fastapi import FastAPI
import pydantic
from enum import Enum
from typing import List


app = FastAPI()


###  Pydantic Input/Output Schemas ###


class PingResponse(pydantic.BaseModel):
    message: str


class VarName(Enum):
    country = "country"
    age_group = "age_group"


class Variable(pydantic.BaseModel):
    var_name: VarName
    category: str


class VariableList(pydantic.BaseModel):
    data: List[Variable]


class Factor(pydantic.BaseModel):
    var_name: VarName
    category: str
    factor: float


class FactorResults(pydantic.BaseModel):
    results: List[Factor]


class ValidationResults(pydantic.BaseModel):
    valid: bool
    message: str


### Routes ###


@app.get("/ping")
async def ping() -> PingResponse:
    return {"message": "PONG"}


@app.post("/validate")
async def validate(data: VariableList) -> ValidationResults:
    return {"valid": False, "message": "TODO"}


@app.post("/get_factors")
async def get_factors(data: VariableList) -> FactorResults:
    return {"results": []}
