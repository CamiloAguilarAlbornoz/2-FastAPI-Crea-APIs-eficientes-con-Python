import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

# Si en el archivo de configuración no encuentra una DATABASE_URL, crea una BD en sqlite
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./blog.db')

engine_kwargs= {}

if DATABASE_URL.startswith('sqlite'):
    engine_kwargs['connect_args'] = {'check_same_thread': False}

# echo muestra que sql se ejecutó en cada consulta
# future indica que se quiere ocupar la sintaxis moderna de sqlalchemy 2
# engine_kwargs se usa únicamente para que funcione con sqlite
engine = create_engine(DATABASE_URL, echo = True, future = True, **engine_kwargs)

# Util para establecer una sesión con la base de datos por cada request
# autoflush no envía cambios hasta hacer el commit, es decir no son cambios automáticos
SessionLocal = sessionmaker(bind = engine, autoflush = False, autocommit = False, class_ = Session)

# Permite definir los modelos ORM como clases
class Base(DeclarativeBase):
    pass

# Funcion para crear la sesión cada que se entre a un endpoint y que la cierre al salir
def get_db():
    db = SessionLocal() # Inicializa la sesión
    try:
        yield db # FastAPI espera una dependencia del tipo generadora, se usa para que la sesión se pause para que cuando el endpoint la use y luego finally la cierre
    finally:
        db.close() # Cierra siempre la sesión de la base de datos