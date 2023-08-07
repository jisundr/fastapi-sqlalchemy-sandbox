from fastapi import APIRouter, Depends, Request
from typing import Annotated


from app.config import Settings
from app.dependencies import get_settings

info_router = APIRouter(tags=["API Info"])


@info_router.get("/")
def get_api_info(
    request: Request, settings: Annotated[Settings, Depends(get_settings)]
):
    base_url = request.base_url
    return {
        "title": settings.APP_NAME,
        "description": settings.APP_DESCRIPTION,
        "version": settings.APP_VERSION,
        "api_docs": f"{base_url}docs",
    }
