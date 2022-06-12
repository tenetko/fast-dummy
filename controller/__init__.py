from fastapi import APIRouter

from .response import router as fast_dummy_router
from .root import router as root_router

api_router = APIRouter()
static_router = APIRouter()

api_router.include_router(fast_dummy_router, prefix="/fast")
static_router.include_router(root_router)
