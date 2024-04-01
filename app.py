from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from sqlalchemy.ext.asyncio import create_async_engine
from starlette.middleware.cors import CORSMiddleware

from config import DefaultSettings
from optimal_route.endpoints import list_routers

settings = DefaultSettings()


def get_app() -> FastAPI:
    """
    Базовая сборка объекта приложения
    :return: объект приложения
    """
    application = FastAPI(
        title="Optimal route",
        docs_url="/swagger",
        version="1.0.0",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    for route in list_routers:
        application.include_router(route, prefix=settings.PATH_PREFIX)
    return application


app = get_app()


@app.on_event("startup")
def startup_db_client():
    app.db_engine = create_async_engine(settings.get_db_connection_url())


@app.on_event("shutdown")
async def shutdown_db_client():
    await app.db_engine.dispose()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"error_type": exc.__class__.__name__, "error_message": str(exc)},
    )
