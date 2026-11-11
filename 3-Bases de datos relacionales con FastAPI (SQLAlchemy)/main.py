from fastapi import Depends, FastAPI, Query, status, Path # Path es util para agregar reglas en los pathparametters
from typing import List, Optional, Union, Literal

from db.db_configure import get_db, start_db
from models.dao.PostCreate import PostCreate
from models.dao.PostPublic import PostPublic
from models.dao.PaginatedPost import PaginatedPost
from models.dao.PostSummary import PostSummary
from models.dao.PostUpdate import PostUpdate
from models.service.delete_service import delete_post_service
from models.service.get_service import filter_by_tags_service, get_post_by_id_service, posts_service
from models.service.post_service import create_post_service
from models.service.update_service import update_post_service

from sqlalchemy.orm import Session

app = FastAPI(title='Mini Blog')

start_db()

################# GET #######################################

@app.get('/')
def home():
    return {'message': 'Bienvenido al Mini Blog por Camilo'}

'''
Util para query que viene con una lista
'''
@app.get('/posts/by-tags', response_model=List[PostPublic], response_model_exclude_none=True)
def filter_by_tags(
    tags: List[str] = Query(
        ...,
        min_length = 1,
        description = 'Una o más etiquetas, ejemplo: ?tags=python&tags=fastapi'
    ),
    db: Session = Depends(get_db)
):
    return filter_by_tags_service(tags, db)


@app.get('/posts', response_model = PaginatedPost, response_model_exclude_none = True)
def posts(
    text: Optional[str] = Query(
        default = None,
        description = 'Buscar por título - Parametro obsoleto, usa query o search en su lugar',
        deprecated = True # Indica que este query o parametro está obsoleto
    ),
    query: Optional[str] = Query(
        default = None,
        description = 'Buscar por título',
        alias = 'search',
        min_length = 3,
        max_length = 50,
        pattern = r'^[\w\sáéíóúÁÉÍÓÚüÜ-]+$' # Expresión regular para que acepte tildes o ¨
    ),
    per_page: int = Query(10, ge = 1, le = 50, description = 'Número de resultados (1 - 50)'), # Cantidad de elementos por págima, 10 por defecto
    page: int = Query(1, ge = 1, description = 'Número de página >= 1'),
    order_by: Literal['id', 'title'] = Query('id', description = 'Campo de orden'),# Indica que solo se puede ingresar a los valores id y title
    direction: Literal['asc', 'desc'] = Query('asc', description = 'Dirección de orden'), # Indica que se pueden ordenar ascendente o descendente
    db: Session = Depends(get_db)
):
    return posts_service(text, query, per_page, page, order_by, direction, db)
    
'''
Se encarga de entregar un Post con el id, recibe un query donde en caso de ser True
entregará también la descripción del post, si es false, no lo entregará

EJEMPLO: my_api/post-query-params/2?includes_content=True
'''
@app.get(
    '/posts/{post_id}',
    response_model=Union[PostPublic, PostSummary],
    response_description='Post encontrado',
    response_model_exclude_none=True
)
def get_post_by_id(
    post_id: int = Path(
        ..., # Indica que si o si debe haber un parámetro
        ge = 1, # Indica que post_id deberá ser mayor o igual a 1
        title = 'ID del Post',
        description = 'Identificador entero del post, debe ser mayor a 1',
        example = 1),
    includes_content: bool = Query(default=True, description='Indica si incluye o no el contenido'),
    db: Session = Depends(get_db)
    ):
    return get_post_by_id_service(post_id, includes_content, db)
    

################# POST #######################################

'''
Se encarga de envía un post

Se eliminan validaciones ya que Pydentic valida
si se ingreso un title y un content

El método funcionara con una sesión que dependera de que la base de datos haya iniciado
'''
@app.post('/posts', response_model=PostPublic, response_model_exclude_none=True, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post_service(post, db)

################# PUT ########################################
@app.put('/posts/{post_id}', response_model=PostPublic, response_model_exclude_none=True, 
         status_code=status.HTTP_201_CREATED)
def update_post(post_id: int, data: PostUpdate, db: Session = Depends(get_db)):
    return update_post_service(post_id, data, db)

################# DELETE #####################################
@app.delete('/posts/{post_id}', response_model_exclude_none=True, status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return delete_post_service(post_id, db)
    