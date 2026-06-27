from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logging import logger
from app.shared.exceptions import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 TenderIQ AI Backend Started")

    yield

    logger.info("🛑 TenderIQ AI Backend Stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
# TenderIQ AI

An AI-powered Government & Enterprise Tender Intelligence System.

## Features
- Government Tender Monitoring
- Enterprise Tender Intelligence
- OCR-Based Tender Extraction
- Machine Learning Qualification Prediction
- Automated Notifications
- Analytics Dashboard
""",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Register Global Exception Handlers
register_exception_handlers(app)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routes
app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
)