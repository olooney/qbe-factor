from fastapi import FastAPI, HTTPException
import pydantic
from typing import List
from .models import VarName, Variable, VariableFactor, FactorModel


app = FastAPI()
model = FactorModel.load()

# these pydantic types are specific to the particular JSON schemas used by the
# REST API so are defined here along with the routes.

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
def ping() -> PingResponse:
    """
    Simple low-overhead PING route to check if the server is up.
    """
    return {"message": "PONG"}


@app.post("/validate")
def validate(variable_list: VariableList) -> ValidationResults:
    """
    Validates input without running the model. Returns either a 422 with a
    validation error message if any errors are found, or a 200 with a simple
    "is valid" message if all variables are valid.
    """
    # All validation occurs as pydantic checks the POSTed JSON against
    # the VariableList schema, including the category/var_name mismatch.
    # If any errors are found it will throw a ValidationError which will
    # return a 422 HTTP response. If we reach this line of code, we know
    # that all input was in fact valid.
    return {"valid": True, "message": "All variables are valid."}


@app.post("/get_factors")
def get_factors(variable_list: VariableList) -> FactorResults:
    """
    Computes the factor for a list of variables. Performs the same validation
    as `/validate`. If a ValueError other occurs during the execution of the
    model, returns a 500 message with an appropriate error message; if an
    unknown or unexpected error occurs, returns a 500 with an opaque error
    message. 
    """
    try:
        variables = variable_list.data
        factors = list(model.get_factors(variables))
        return {"results": factors}
    except ValueError as ex:
        raise HTTPException(status_code=500, detail=ex.args[0])
