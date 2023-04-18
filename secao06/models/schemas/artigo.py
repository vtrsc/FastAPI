from  sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings



class ArtiModel(settings.DBBaseModel):
    _tablename_ = 'artigos'
    
    id =Column(Integer , primary_key=True , autoincrement=True)
    titulo = Column(String(256))
    url_fonte = Column(Integer , ForeignKey('usuarios.id'))
    usuario_id = Column(Integer , ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='artigos' , lazy='joined')