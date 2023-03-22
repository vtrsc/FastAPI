from typing  import Optional    
from pydantic import BaseModel as SCBaseMOdel   



class CursoSchema(SCBaseMOdel): 
    id: Optional[int]   
    titulo: str 
    aulas: int
    horas: int      

    class Config:   
        orm_mode = True
