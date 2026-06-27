from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger
from app.api.v1.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("TenderIQ AI Backend Started")
    yield
    logger.info("TenderIQ AI Backend Stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(
    health_router,
    prefix=settings.API_PREFIX
)