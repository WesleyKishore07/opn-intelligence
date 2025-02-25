# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import create_v1_router


def create_root_app() -> FastAPI:
    app = FastAPI(
        title="OPN Intelligence",
        description="Combined API for all OPN Intelligence services",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create and include v1 router
    app.include_router(create_v1_router())

    return app

app = create_root_app()