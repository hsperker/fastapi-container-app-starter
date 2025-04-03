from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.responses import Response
from typing import Union

def validation_exception_handler(request: Request, exc: RequestValidationError) -> Union[Response, JSONResponse]:
    """
    Custom exception handler for validation errors
    Returns a cleaner error format with status code 422
    """
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body}
    )