from fastapi import FastAPI
from src.person.routes import router

version = "v1"

app = FastAPI(
    title="Person Data",
    description="A REST API for people",
    version=version
    
)

app.include_router(router, prefix = "/person")