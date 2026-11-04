from math import ceil
from fastapi import FastAPI, Query, HTTPException, status, Path # Path es util para agregar reglas en los pathparametters
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import List, Optional, Union, Literal

app = FastAPI(title='Mini Blog')

BLOG_POST = [
    {'id': 1, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 2, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 3, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 4, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 5, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 6, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 7, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 8, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 9, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 10, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 11, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 12, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 13, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 14, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 15, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 16, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post', 'tags': [{'name': 'fastapi'}]},
    {'id': 17, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 18, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 19, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 20, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 21, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 22, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 23, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 24, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 25, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 26, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 27, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 28, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 29, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 30, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},
    {'id': 31, 'title': 'Hola desde FastAPI', 'content': 'Mi primer post'},
    {'id': 32, 'title': 'Mi segundo POST con FastAPI', 'content': 'Mi segundo POST con FastAPI'},
    {'id': 33, 'title': 'DJango vs FastAPI', 'content': 'FastAPI es más rapido'},

]

class Tag(BaseModel):
    
    name: str = Field(..., min_length=2, max_length=30, description='Nombre de la etiqueta')

class Author(BaseModel):
    
    name: str = Field(..., min_length=5, max_length=30, description='Nombre del autor')
    email: EmailStr  = Field(..., min_length=10, max_length=30, description='Email del autor')

class PostBase(BaseModel):
    
    title: str
    content: str
    tags: Optional[List[Tag]] = Field(default_factory = list) # Crea una lista vacía, creando una por cada objeto que se crea en el programa
    author: Optional[Author] = None

class PostCreate(BaseModel):
    
    title: str = Field(
        ..., # Indica que el campo es obligatorio, elipsis
        min_length=3, # Indica que el campo debe tener un mínimo de 3 caracteres
        max_length=100, # Indica que el campo deberá tener máximo 100 caracteres
        description='Titulo del Post (mínimo 3 caracteres y máximo 100)', # Descripción del campo
        examples=['Mi primer post con fastAPI'] # Ejemplo que verá el usuario en la documentación
    )
    content: Optional[str] = Field(
        default='Contenido pendiente...', # Valor por defecto del campo
        min_length=10,
        description='Contenido del post (mínimo 10 caracteres)',
        examples=['Este es un contenido valido porque tiene 10 caracteres o más']
    )
    tags: List[Tag] = Field(default_factory = list)
    author: Optional[Author] = None
    
    '''
    Se encarga de evaluar el title de forma más avanzada
    '''
    @field_validator('title') # Evalua el campo que se ingrese por parametro, title en este caso
    @classmethod # Indica que se va a ocupar la clase completa, util para evaluarla completamente
    def not_allowed_title(cls, value: str) -> str:
        words_not_allowd = ['porn', 'xxx', 'count', 'pussy', 'cock', 'dick', 'spam']
        for word in words_not_allowd:
            if word in value.lower():
                raise ValueError(f'El título no puede contener la palabra {word}')
        return value

class PostUpdate(BaseModel):
    
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    content: Optional[str] = None # Indica que el content es opcional, se usa None para que en caso de una actualización se conserve lo que ya se tenía

class PostPublic(PostBase):
    
    id: int
    
class PostSummary(BaseModel):
    
    id: int
    title: str

class PaginatedPost(BaseModel):
    
    page: int
    per_page: int
    total: int
    total_pages: int
    has_prev: bool
    has_next: bool
    order_by: str
    direction: str
    search: Optional[str]
    items: List[PostPublic]

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
        min_length = 2,
        description = 'Una o más etiquetas, ejemplo: ?tags=python&tags=fastapi'
    )
):
    tags_lower = [tag.lower() for tag in tags]
    return [
        post for post in BLOG_POST if any(tag['name'].lower() in tags_lower for tag in post.get('tags', []))
    ]

'''
El parametro es opcional y hace referencia a los
queryParameters

el default=None indica que por defecto este endpoint no recibe queryparameter

el response_model es para indicar como va a llegar la respuesta, en este caso será un listado de PostPublic

EJEMPLO: my_api/posts?query=holaaaaa
'''
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
        alias = 'search', # Esto es para que la query en el api se vea con otra palabra, search en este caso /posts?search=django
        min_length = 3,
        max_length = 50,
        pattern = r'^[\w\sáéíóúÁÉÍÓÚüÜ-]+$' # Expresión regular para que acepte tildes o ¨
    ),
    per_page: int = Query(10, ge = 1, le = 50, description = 'Número de resultados (1 - 50)'), # Cantidad de elementos por págima, 10 por defecto
    page: int = Query(1, ge = 1, description = 'Número de página >= 1'),
    order_by: Literal['id', 'title'] = Query('id', description = 'Campo de orden'),# Indica que solo se puede ingresar a los valores id y title
    direction: Literal['asc', 'desc'] = Query('asc', description = 'Dirección de orden') # Indica que se pueden ordenar ascendente o descendente):
):
    results = BLOG_POST
    if query:
        results = []
        for post in BLOG_POST:
           if query.lower() in post['title'].lower():
               results.append(post)
    total = len(results)
    results = sorted(results, key = lambda post: post[order_by], reverse = (direction == 'desc')) # Indica que dependiendo el order_by, se regresará un post vía lamda, el reverse indica en que orden se mostrará
    total_pages = ceil(total / per_page) if total > 0 else 0
    if total_pages != 0:
        current_page = min(page, total_pages)
    else: current_page = 1
    if total_pages == 0:
        items = []
    else:
        start = (current_page - 1) * per_page
        items = results[start: start + per_page] # Se indica desde donde se inicia y hasta donde va
    has_prev = page != 1
    has_next = page != total_pages
    return PaginatedPost(
        per_page = per_page,
        items = items,
        total = total,
        total_pages = total_pages,
        page = current_page,
        has_prev = has_prev,
        has_next = has_next,
        order_by = order_by,
        direction = direction,
        search = query
    )

'''
Lo mismo del de arriba pero con un
list complejation
'''
@app.get('/posts-list-complejation', response_model = PaginatedPost, response_model_exclude_none = True)
def posts_list_complejetion(query: Optional[str] = Query(
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
    direction: Literal['asc', 'desc'] = Query('asc', description = 'Dirección de orden') # Indica que se pueden ordenar ascendente o descendente
):
    results = BLOG_POST
    if query: results = [post for post in results if query.lower() in post['title'].lower()]
    total = len(results)
    results = sorted(results, key = lambda post: post[order_by], reverse = (direction == 'desc')) # Indica que dependiendo el order_by, se regresará un post vía lamda, el reverse indica en que orden se mostrará
    total_pages = ceil(total / per_page) if total > 0 else 0
    if total_pages != 0:
        current_page = min(page, total_pages)
    else: current_page = 1
    if total_pages == 0:
        items = []
    else:
        start = (current_page - 1) * per_page
        items = results[start: start + per_page] # Se indica desde donde se inicia y hasta donde va
    has_prev = page != 1
    has_next = page != total_pages
    return PaginatedPost(
        per_page = per_page,
        items = items,
        total = total,
        total_pages = total_pages,
        page = current_page,
        has_prev = has_prev,
        has_next = has_next,
        order_by = order_by,
        direction = direction,
        search = query
    )

'''
Filtra enviando un dato por link pero no como query sino como parametro

EJEMPLO: my_api/posts/4

Union da la posibilidad de que FastAPI evalue los dos modelos, es decir evaua el primero que es PostPublic
y si cumple retorna con ese modelo, de lo contrario devuelve PostSummary
'''
@app.get(
    '/posts/{post_id}',
    response_model=Union[PostPublic, PostSummary],
    response_description='Post encontrado',
    response_model_exclude_none=True
)
def get_post_by_id(post_id : int = Path(
    ..., # Indica que si o si debe haber un parámetro
    ge = 1, # Indica que post_id deberá ser mayor o igual a 1
    title = 'ID del Post',
    description = 'Identificador entero del post, debe ser mayor a 1',
    example = 1)):
    for post in BLOG_POST:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post no encontrado {post_id}')

'''
Se encarga de entregar un Post con el id, recibe un query donde en caso de ser True
entregará también la descripción del post, si es false, no lo entregará

EJEMPLO: my_api/post-query-params/2?includes_content=True
'''
@app.get(
    '/post-query-params/{post_id}',
    response_model=Union[PostPublic, PostSummary],
    response_description='Post encontrado',
    response_model_exclude_none=True
)
def get_post_by_id_with_or_not_content(post_id: int = Path(
    ..., # Indica que si o si debe haber un parámetro
    ge = 1, # Indica que post_id deberá ser mayor o igual a 1
    title = 'ID del Post',
    description = 'Identificador entero del post, debe ser mayor a 1',
    example = 1), includes_content: bool = Query(default=True, description='Indica si incluye o no el contenido')):
    for post in BLOG_POST:
        if post['id'] == post_id:
            print(f'LLegaaaaaaaaaaaaaaaaaa = {post}')
            if includes_content: return post
            return {
                'id': post['id'],
                'title': post['title']
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post no encontrado {post_id}')

################# POST #######################################

'''
Se encarga de envía un post

Se eliminan validaciones ya que Pydentic valida
si se ingreso un title y un content
'''
@app.post('/posts', response_model=PostPublic, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id = (BLOG_POST[-1]['id'] + 1) if BLOG_POST else 1 # Obtiene el ultimo ID
    new_post = {
        'content': post.content,
        'title': post.title,
        'id': new_id,
        'tags': [tag.model_dump() for tag in post.tags],
        'author': post.author.model_dump() if post.author else None
    }
    BLOG_POST.append(new_post)
    return new_post

################# PUT ########################################
@app.put('/posts/{post_id}', response_model=PostPublic, response_model_exclude_none=True, 
         status_code=status.HTTP_201_CREATED)
def update_post(post_id: int, data: PostUpdate):
    for post in BLOG_POST:
        if post['id'] == post_id:
            playload = data.model_dump(exclude_unset=True) # Convierte la data en un diccionario, excluye valores que no se envíen
            if 'title' in playload : post['title'] = data.title
            if 'content' in playload: post['content'] = data.content
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post no encontrado')

################# DELETE #####################################
@app.delete('/posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POST):
        if post['id'] == post_id:
            BLOG_POST.pop(index)
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post no encontrado')