from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_model import CursoModel
from core.deps import get_session


# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar  


SelectOfScalar.inherit_cache = True # type: ignore   
Select.inherit_cache = True # type: ignore
# Fim Bypass



router = APIRouter()

# POST CURSO

@router.post('/',status_code=status.HTTP_201_CREATED , response_model=CursoModel)   
async def post_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):   
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)  
    db.add(novo_curso)  
    await db.commit()
    return novo_curso   



# GET CURSO 
@router.get('/',response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:   
        query = select(CursoModel)  
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()   
        return cursos
    
# PUT CURSO 

@router.put('/',status_code=status.HTTP_202_ACCEPTED , response_model=CursoModel)
async def put_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):    
    async with db as session:   
        query = select(CursoModel).filter(CursoModel.id == curso.id)   
        result = await session.execute(query)   
        curso_db = result.scalar_one_or_none()   
        if curso_db:   
            curso_db.titulo = curso.titulo   
            curso_db.aulas = curso.aulas   
            curso_db.horas = curso.horas   
            await session.commit()   
            return curso_db   
        else:   
            raise HTTPException(detail='curso nao encontrado',   
                                status_code=status.HTTP_404_NOT_FOUND)    

