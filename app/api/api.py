from fastapi import APIRouter

from app.api.endpoints import block

api_router = APIRouter()
api_router.include_router(block.router)
