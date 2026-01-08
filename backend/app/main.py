from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

# Importamos lo que ya habías creado de la DB
from .database import SessionLocal, engine, Base, Feedback

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuramos la carpeta de HTML
templates = Jinja2Templates(directory="app/templates")

# Dependencia de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# RUTA 1: Servir la página principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# RUTA 2: Recibir feedback y devolver un componente HTML (HTMX style)
@app.post("/feedback")
async def create_feedback(user: str = Form(...), comment: str = Form(...), db: Session = Depends(get_db)):
    db_item = Feedback(user=user, comment=comment)
    db.add(db_item)
    db.commit()
    # Devolvemos solo el "pedazo" de HTML para la lista
    return f"""
    <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl mb-4 border-l-4 border-blue-500 shadow-lg animate-in fade-in slide-in-from-left-4">
        <div class="flex justify-between items-start mb-2">
            <span class="font-bold text-blue-400">{user}</span>
            <span class="text-xs text-slate-500 uppercase tracking-widest">PostgreSQL Storage</span>
        </div>
        <p class="text-slate-300 leading-relaxed">{comment}</p>
    </div>
    """

# RUTA 3: Listar todos los feedbacks al cargar la página
@app.get("/feedback")
async def list_feedback(db: Session = Depends(get_db)):
    items = db.query(Feedback).order_by(Feedback.id.desc()).all()
    html_content = ""
    for item in items:
        html_content += f"""
        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl mb-4 border-l-4 border-slate-700 shadow-lg">
            <div class="flex justify-between items-start mb-2">
                <span class="font-bold text-blue-400">{item.user}</span>
                <span class="text-xs text-slate-500 font-mono italic text-[10px]">ID: {item.id}</span>
            </div>
            <p class="text-slate-300">{item.comment}</p>
        </div>
        """
    return HTMLResponse(content=html_content)