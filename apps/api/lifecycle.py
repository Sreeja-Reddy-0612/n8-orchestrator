from core.persistence.database import Base, engine
from core.persistence.checkpoint import init_db


def register_lifecycle_events(app):

    @app.on_event("startup")
    def startup_event():
        init_db()