# INSTRUCCIONES PARA LEVANTAR EL PROYECTO #######################################################################

1) Levantar un entorno virtual. [python -m venv venv] o [py -3.13 -m venv venv]
2) Acceder al entorno virtual.  [.\venv\Scripts\activate]
3) Instalar FastAPI             [pip install "fastapi[standard]"]
5) Ejecutar un .py con fastapi. [fastapi dev .\main.py] o [uvicorn main:app --reload]
4) Salir del entorno virtual.   [.\venv\Scripts\deactivate]

# BASES DE DATOS RELACIONALES CON FAST API #######################################################################

1) Instalar SQLAlchemy, util para el ORM de SQL.                   [pip install "sqlalchemy"]
2) Instalar driver para conectar las bases de datos a PostgreSQL.  [pip install "psycopg[binary]"]
3) Las tablas se representan con clases que representen los modelos en la base de datos

# COMO VER LA BASE DE DATOS EN EL CONTENEDOR DE DOCKER

1) Crea el contenedor y la base de datos en Docker.              [docker-compose up -d]
2) Ingresa a psql en el contenedor e ingresa a la base de datos. [psql -U camilodb_owner -d deviblog]
3) Para listar los usuarios y sus privilegios                    [\du]
4) Para listar las bases de datos                                [\l]
5) Para listar las tablas de la base de datos                    [\dt]