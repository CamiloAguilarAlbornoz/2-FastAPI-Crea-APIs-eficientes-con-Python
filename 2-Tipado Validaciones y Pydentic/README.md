# INSTRUCCIONES PARA LEVANTAR EL PROYECTO #######################################################################

1) Levantar un entorno virtual. [python -m venv venv] o [py -3.13 -m venv venv]
2) Acceder al entorno virtual.  [.\venv\Scripts\activate]
3) Instalar FastAPI             [pip install "fastapi[standard]"]
5) Ejecutar un .py con fastapi. [fastapi dev .\main.py] o [uvicorn main:app --reload]
4) Salir del entorno virtual.   [.\venv\Scripts\deactivate]

# INSTRUCCIONES PARA LEVANTAR EL PROYECTO #######################################################################

#### Que es Pydantic
Es una librería de Python que permite definir y validar datos usando clases. Solo definimos y Pydantic se encarga de validarlos, transformarlos y darnos objetos listos para usar

#### Porque lo usa FastAPI
1) Por validación automática, lo cual es validación de tipos, como string, int, etc.
2) Ayuda para la documentación automática
3) Ayuda a la conversión de datos
4) Seguridad y consistencia de la información
5) Esta diseñado para trabajar con tipado estático

#### Pydantic 1 vs Pydantic 2
Pydantic 1 está hecho para proyectos antiguos o librerías que aún no se migran al 100% a Pydantic 2, Pydantic 2 es una versión mucho más actualizada y con soporte mucho más amplio que el de Pydantic 1, Pydantic 1 se realizó con python y Pydantic 2 se generó con Pydantic core, el cual se implementó con rust y se conecta con Python con bindings. El consumo de memoria de Pydantic 2 es muchisimo menor que el de Pydantic 1, además que es más veloz