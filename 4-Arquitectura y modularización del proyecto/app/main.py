from dotenv import load_dotenv
from fastapi import FastAPI

from app.core.db import Base, engine
from app.api.v1.post.router import router as post_router
from app.api.v1.tags.router import router as tag_router

from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI(title='Mini Blog')
    Base.metadata.create_all(bind = engine) # DEV => Crea las tablas en caso no existan, SOLO EN DEV
    app.include_router(post_router) # Incluye las rutas de post en el router
    app.include_router(tag_router) # Incluye las rutas de tags en el router
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            'http://localhost:5173',
        ],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return app

load_dotenv() # Busca el .env
app = create_app()