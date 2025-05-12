from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import SolicitacaoAcesso, Usuario, Tabela
from app.routers.users import fake_sessions

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/aprovacoes")
def listar_aprovacoes(request: Request, db: Session = Depends(get_db)):
    steward_id = fake_sessions.get("usuario")
    if not steward_id:
        return RedirectResponse("/login", status_code=302)

    solicitacoes = (
        db.query(SolicitacaoAcesso)
        .join(Tabela)
        .filter(Tabela.data_steward_id == steward_id)
        .filter(SolicitacaoAcesso.status == "pendente")
        .all()
    )

    for s in solicitacoes:
        s.solicitante = db.query(Usuario).filter(Usuario.id == s.solicitante_id).first()
        s.tabela = db.query(Tabela).filter(Tabela.id == s.tabela_id).first()

    return templates.TemplateResponse("aprovacoes.html", {"request": request, "solicitacoes": solicitacoes})


@router.post("/aprovar/{solicitacao_id}")
def decidir_aprovacao(
    solicitacao_id: int,
    acao: str = Form(...),
    db: Session = Depends(get_db)
):
    solicitacao = db.query(SolicitacaoAcesso).filter(SolicitacaoAcesso.id == solicitacao_id).first()
    if solicitacao:
        if acao == "aprovar":
            solicitacao.status = "aprovado"
        elif acao == "rejeitar":
            solicitacao.status = "rejeitado"
        db.commit()

    return RedirectResponse("/solicitacoes/aprovacoes", status_code=302)
