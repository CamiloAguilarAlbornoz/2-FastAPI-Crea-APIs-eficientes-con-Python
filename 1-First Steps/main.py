from fastapi import Body, FastAPI, Query, HTTPException, status

app = FastAPI(title='Mini Blog')

BLOG_POST = [
    {'id': 1, 'title': 'Hola desde FastAPI', 'Content': 'Mi primer post'},
    {'id': 2, 'title': 'Mi segundo POST con FastAPI', 'Content': 'Mi segundo POST con FastAPI'},
    {'id': 3, 'title': 'DJango vs FastAPI', 'Content': 'FastAPI es más rapido'}
]

################# GET #######################################

@app.get('/')
def home():
    return {'message': 'Bienvenido al Mini Blog por Camilo'}

'''
El parametro es opcional y hace referencia a los
queryParameters

el default=None indica que por defecto este endpoint no recibe queryparameter

EJEMPLO: my_api/posts?query=holaaaaa
'''
@app.get('/posts')
def posts(query: str | None = Query(default=None, description='Buscar por título')):
    if query:
        results = []
        for post in BLOG_POST:
           if query.lower() in post['title'].lower():
               results.append(post)
        return {'data': results, 'query': query}
    return {'data': BLOG_POST}

'''
Lo mismo del de arriba pero con un
list complejation
'''
@app.get('/posts-list-complejation')
def posts_list_complejetion(query: str | None = Query(default=None, description='Buscar por título')):
    if query == None : return {'data': BLOG_POST}
    results = [post for post in BLOG_POST if query.lower() in post['title'].lower()]
    return {'data': results, 'query': query}

'''
Filtra enviando un dato por link pero no como query sino como parametro

EJEMPLO: my_api/posts/4
'''
@app.get('/posts/{post_id}')
def get_post_by_id(post_id : int):
    for post in BLOG_POST:
        if post['id'] == post_id:
            return {'data': post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post no encontrado {post_id}')

'''
Se encarga de entregar un Post con el id, recibe un query donde en caso de ser True
entregará también la descripción del post, si es false, no lo entregará

EJEMPLO: my_api/post-query-params/2?includes_content=True
'''
@app.get('/post-query-params/{post_id}')
def get_post_by_id_with_or_not_content(post_id: int,
                                       includes_content: bool = Query(default=True, 
                                                                      description='Indica si incluye o no el contenido')):
    for post in BLOG_POST:
        if post['id'] == post_id:
            if includes_content: return {'data': post}
            return {
                'data': {
                    'id': post['id'],
                    'title': post['title']
                }
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post no encontrado {post_id}')

################# POST #######################################

'''
Se encarga de envía un post

el ... indica que es obligario pero no ha llegado el contenido

el dict indica que el parametro es de tipo diccionario
'''
@app.post('/posts')
def create_post(post: dict = Body(...)):
    if 'title' not in post or 'content' not in post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Title y Content son requeridos')
    if not str(post['title']).strip(): # Elimina los espacios del string y valida que tenga contenido
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Title no puede estar vacío')
    new_id = (BLOG_POST[-1]['id'] + 1) if BLOG_POST else 1 # Toma el ultimo id y le suma 1 para mantener la secuencia
    new_post = {'id': new_id, 'title': post['title'], 'content': post['content']}
    BLOG_POST.append(new_post)
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f'Post creado')

################# PUT ########################################
@app.put('/posts/{post_id}')
def update_post(post_id: int, data: dict = Body(...)):
    for post in BLOG_POST:
        if post['id'] == post_id:
            if 'title' in data :
                post['title'] = data['title']
            if 'content' in data:
                post['content'] = data['content']
            raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f'Post actualizado')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post no encontrado')

################# DELETE #####################################
@app.delete('/posts/{post_id}')
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POST):
        if post['id'] == post_id:
            BLOG_POST.pop(index)
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Post eliminado correctamente')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post no encontrado')