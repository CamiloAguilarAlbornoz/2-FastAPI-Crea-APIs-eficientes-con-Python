#### INSTRUCCIONES PARA LEVANTAR EL PROYECTO #######################################################################

1) Levantar un entorno virtual. [python -m venv venv] o [python -3.13 -m venv venv]
2) Acceder al entorno virtual.  [.\venv\Scripts\activate]
3) Instalar FastAPI             [pip install "fastapi[standard]"]
5) Ejecutar un .py con fastapi. [fastapi dev .\main.py] o [uvicorn main:app --reload]
4) Salir del entorno virtual.   [.\venv\Scripts\deactivate]

#### METODOS HTTP ##################################################################################################

# GET
Solicita la recuperación de un recurso específico, solo recupera datos.

# POST
Envía una entidad a un recurso específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

# PUT
Reemplaza todas las representaciones actuales del recurso de destino con la carga util de la petición

# DELETE
Borra un recurso específico

# PATCH
Es utilizado para aplicar modificaciones parciales a un recurso

#### HTTP STATUS CODE ##############################################################################################

## 2xx Success ###################################

# 200 Success/OK
Todo salio bien

# 201 Created
Se creó un nuevo recurso

# 202 Accepted
Se aceptó la petición pero no se procesó

## 3xx Redirection ###############################

# 301 Permanent Redirection
El recurso al que se quiere acceder se movio de forma permanente

# 302 Temporary Redirection
El recurso al que se quiere acceder no es accesible

# 303 Not Modified
El recurso no se modificó

## 4xx Client Error ##############################

# 401 Unauthorized Error
Indica que el cliente no tiene autorización para acceder al recurso

# 403 Forbidden
Indica que aunque haya autenticación, hay partes del recurso a las que no hay acceso para el cliente

# 404 Not Found
Indica que el recurso no está presente, ya sea porque no se creó o no está disponible

## 5xx Server Error ##############################

# 501 Not Implemented
Indica que el servidor no soporta la funcionalidad

# 502 Bad Gateway
Indica que el servidor recibio una respuesta invalida de otro servidor

# 503 Service Unavaliable
Indica que el servicio no está disponible, podría ser una sobrecarga o que está en mantenimiento el servidor

#### PETICIONES POST, PUT, DELETE, PATCH  ##########################################################################

# Por CURL
curl -X POST http://127.0.0.1:8000/posts - H "Content-Type: application/json" -d "{'title': 'Enviado desde CURL', 'content': 'Petición POST ejecutada desde CURL'}"

#### DOCUMENTACIÓN AUTOMÁTICA  #####################################################################################

# Swagger
http://127.0.0.1:8000/docs

# Redoc
http://127.0.0.1:8000/redoc