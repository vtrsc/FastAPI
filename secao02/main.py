
from typing import Dict, List, Optional, Any    
from fastapi.responses import JSONResponse      
from fastapi import Response
from fastapi import FastAPI 
from fastapi import HTTPException  
from fastapi import status
from models import Curso    
from fastapi import Path    
from fastapi import Depends             
from time   import sleep



def fake_db():  
     try:   
          print('Abrindo conexao com BD...')    
          sleep(1)  
     finally:   
          print('fechando conexao com BD...')   
          sleep(1)

app = FastAPI() 
    
cursos = { 
1: {    
    "titulo":"bla bla 1", 
    "aulas": 112,   
    "horas": 34
} , 

2:{ 
    "titulo": "bla bla 2",  
    "aulas": 113,   
    "horas": 45
},  

 }      

@app.get('/cursos')  
async def get_cursos(db: Any = Depends(fake_db)): 
    return cursos       

@app.get('/cursos/{curso_id}')    
async def get_curso(curso_id: int = Path(default=None , title='ID do curso' , description='DEve ser entre 1 e 2', gt=0, lt=3) , db: Any = Depends(fake_db)):     
    try:
        curso = cursos[curso_id]        
        return curso    
    except KeyError:    
        raise HTTPException(    
        status_code=status.HTTP_404_NOT_FOUND, detail='Curso n encontrado'
        )
    
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso , db:Any = Depends(fake_db)):
        next_id: int = len(cursos) + 1      
        del curso.id

        cursos[next_id] = curso

        return curso    
    
@app.put('/cursos/{curso_id}') 
async def put_curso(curso_id: int, curso: Curso ,  db:Any = Depends(fake_db)):  
     if curso_id in cursos: 
          cursos[curso_id] = curso                          
          del curso_id
          return curso        
     
     else:   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  
                             detail=f'Nao existe um curso com ID{curso_id}')


@app.delete('/cursos/{curso_id}') 
async def delete_cursos(curso_id:int ,  db:Any = Depends(fake_db)):   
     if curso_id in cursos: 
          del cursos[curso_id] 
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,) 
          return Response(status_code=status.HTTP_204_NO_CONTENT,)    
     else:  
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,    
                              detail=f'iD{curso_id} nao existe')



if __name__ == '__main__':  

    import uvicorn  
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)