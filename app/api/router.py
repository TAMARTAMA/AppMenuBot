from fastapi import APIRouter
from app.api.routes import webhook, health

api_router = APIRouter()

api_router.include_router(webhook.router, prefix="/webhook", tags=["Webhook"])
api_router.include_router(health.router, prefix="/health", tags=["Health"])
