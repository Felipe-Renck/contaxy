from typing import Any

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from loguru import logger
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, RedirectResponse

from contaxy import __version__, config
from contaxy.api.endpoints import (
    auth,
    deployment,
    extension,
    file,
    project,
    system,
    user,
)
from contaxy.api.state import GlobalState
from contaxy.schema.exceptions import UnifiedError
from contaxy.utils import fastapi_utils

# Initialize API
app = FastAPI(
    title="Contaxy API",
    description="Functionality to create and manage projects, services, jobs, and files.",
    version=__version__,
)

fastapi_utils.add_timing_info(app)

# Exception Handling


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):  # type: ignore
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            UnifiedError(code=exc.status_code, message=exc.detail)
        ),
    )


# Startup and shutdown events


@app.on_event("startup")
def on_startup() -> None:
    """Initializes the global app state object."""
    logger.info("Starting API server instance.")
    GlobalState(app.state).settings = config.settings


@app.on_event("shutdown")
def on_shutdown() -> None:
    """Closes the global app state object.

    This also calls all registered close callback functions.
    """
    logger.info("Stopping API server instance.")
    GlobalState(app.state).close()


if config.settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in config.settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Redirect to docs
@app.get("/", include_in_schema=False)
def root() -> Any:
    return RedirectResponse("./docs")


app.include_router(system.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(project.router)
app.include_router(deployment.job_router)
app.include_router(deployment.service_router)
app.include_router(extension.router)
app.include_router(file.router)

# Patch Fastapi to allow relative path resolution.
fastapi_utils.patch_fastapi(app)
