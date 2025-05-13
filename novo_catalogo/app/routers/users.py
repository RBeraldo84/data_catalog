from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Usuario

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Simula uma sessão básica em memória
fake_sessions = {}

@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "erro": None})

@router.post("/login")
def login(request: Request, email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return templates.TemplateResponse("login.html", {"request": request, "erro": "Usuário não encontrado"})

    # Sessão simples baseada em e-mail (não seguro para produção)
    fake_sessions["usuario"] = usuario.id

    if usuario.papel == "steward":
        return RedirectResponse("/solicitacoes/aprovacoes", status_code=302)
    else:
        return RedirectResponse("/catalogo", status_code=302)
