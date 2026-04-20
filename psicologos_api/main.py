from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import Models
from database import engine, SessionLocal, Base
import insert_data

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔍 Obtener todos los psicólogos
@app.get("/psicologos")
def get_psicologos(db: Session = Depends(get_db)):
    return db.query(Models.Psicologo).all()

# ➕ Crear psicólogo
@app.post("/psicologos")
def create_psicologo(psicologo: dict, db: Session = Depends(get_db)):
    nuevo = Models.Psicologo(**psicologo)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/psicologos/{id}")
def obtener_psicologo(id: int, db: Session = Depends(get_db)):
    psicologo = db.query(Models.Psicologo).filter(Models.Psicologo.id == id).first()
    if not psicologo:
        return {"error": "No encontrado"}
    return psicologo

@app.on_event("startup")
def startup():
    db = SessionLocal()
    insert_data.ingreso()
    db.close()