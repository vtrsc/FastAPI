from  sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings



class UsuarioModel(settings.DBBaseModel):
    _tablename_ = 'artigos'
    
    id =Column(Integer , primary_key=True , autoincrement=True)
    nome = Column(String(256) , nullable=True)
    sobrenom = Column(String(256), nullable=True)
    email = Column(String(256), index=True , nullable=False,unique=True)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(bool , default=False)
    artigos = relationship(
        "ArtigoMopdel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )