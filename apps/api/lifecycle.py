from fastapi import FastAPI
from core.tools.builtins import register_builtin_tools


def register_lifecycle_events(app: FastAPI):

    @app.on_event("startup")
    async def startup_event():
        register_builtin_tools()