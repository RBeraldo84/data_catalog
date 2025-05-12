from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Tabela, Coluna, Usuario, SolicitacaoAcesso
from app.routers.users import fake_sessions

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("")
def ver_catalogo(request: Request, db: Session = Depends(get_db)):
    usuario_id = fake_sessions.get("usuario")
    if not usuario_id:
        return RedirectResponse("/login", status_code=302)

    tabelas = db.query(Tabela).all()
    for t in tabelas:
        t.data_steward = db.query(Usuario).filter(Usuario.id == t.data_steward_id).first()
        t.colunas = db.query(Coluna).filter(Coluna.tabela_id == t.id).all()
        # Verifica o status da solicitação de acesso do usuário
        solicitacao = db.query(SolicitacaoAcesso).filter_by(tabela_id=t.id, solicitante_id=usuario_id).first()
        if solicitacao:
            t.status_solicitacao = solicitacao.status
        else:
            t.status_solicitacao = None

    return templates.TemplateResponse("index.html", {"request": request, "tabelas": tabelas})

@router.post("/solicitar-acesso/{tabela_id}")
def solicitar_acesso(tabela_id: int, request: Request, db: Session = Depends(get_db)):
    usuario_id = fake_sessions.get("usuario")
    if not usuario_id:
        return RedirectResponse("/login", status_code=302)

    # Verifica se já existe solicitação
    existente = db.query(SolicitacaoAcesso).filter_by(tabela_id=tabela_id, solicitante_id=usuario_id).first()
    if not existente:
        nova = SolicitacaoAcesso(status="pendente", tabela_id=tabela_id, solicitante_id=usuario_id)
        db.add(nova)
        db.commit()

    return RedirectResponse("/catalogo", status_code=302)
