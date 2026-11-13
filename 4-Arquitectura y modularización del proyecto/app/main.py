from dotenv import load_dotenv
from fastapi import FastAPI

from app.core.db import Base, engine
from app.api.v1.post.router import router as post_router

def create_app() -> FastAPI:
    app = FastAPI(title='Mini Blog')
    Base.metadata.create_all(bind = engine) # DEV => Crea las tablas en caso no existan, SOLO EN DEV
    app.include_router(post_router) # Incluye las rutas de post en el router
    return app

load_dotenv() # Busca el .env
app = create_app()