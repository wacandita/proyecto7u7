from pydantic import BaseModel

class PsicologoBase(BaseModel):
    nombre: str
    descripcion: str
    correo: str
    ubicacion: str
    imagen: str

class PsicologoCreate(PsicologoBase):
    pass

class PsicologoResponse(PsicologoBase):
    id: int

    class Config:
        orm_mode = True