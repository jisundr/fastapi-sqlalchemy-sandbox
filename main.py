from fastapi import FastAPI

from app.api import info_router, dataset_router

app = FastAPI()

app.include_router(info_router)
app.include_router(dataset_router)
