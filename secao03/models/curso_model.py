from core.configs import settings   
from sqlalchemy import Column , Integer , String    

class CursoModel(settings.DBBaseMOdel):
       __tabkename__ = 'cursos' 

       id: Column(Integer, primary_key=True , autoincrement=True)   
       titulo: str= Column(String(100))    
       aulas: int = Column(Integer) 
       horas: int = Column(Integer)
                          