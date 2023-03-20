from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int  # mais de 12
    horas: int  # mais de 10




cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Algoritmos e Lógica de Programação', aulas=52, horas=66),
] 