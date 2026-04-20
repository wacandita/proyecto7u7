from sqlalchemy import Column, Integer, String
from database import Base

class Psicologo(Base):
    __tablename__ = "psicologos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    correo = Column(String)
    ubicacion = Column(String)
    imagen = Column(String)