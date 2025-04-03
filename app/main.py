import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.exceptions import RequestValidationError

from app.api.routers import system, items
from app.api.middleware import validation_exception_handler

app = FastAPI(
    title="FastAPI Hexagonal Architecture",
    description="A sample API built with FastAPI following hexagonal architecture",
    version="0.1.0"
)

# Register exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore[arg-type]

# Register routers
app.include_router(system.router)
app.include_router(items.router)

@app.get("/", include_in_schema=False)
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url='/docs')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)