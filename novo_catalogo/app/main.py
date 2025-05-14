from fastapi import FastAPI #, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers import catalog, users, requests
#from services.pdf_generator import gerar_pdf

app = FastAPI()

# Arquivos estáticos (fotos, CSS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Registra os templates do Jinja2
templates = Jinja2Templates(directory="templates")

# Inclui os módulos de rotas
app.include_router(users.router, prefix="")
app.include_router(catalog.router, prefix="/catalogo")
app.include_router(requests.router, prefix="/solicitacoes")

# @app.post('/solicitacoes/{id}')
# async def processar_solicitacao(id: int, request: Request, acao: str = Form(...)):
#     solicitacao = solicitacao.query.get(id)
#     steward = steward.query.first()  # Ajuste conforme necessário

#     if acao == 'aprovar':
#         # Lógica para aprovar a solicitação
#         pass
#     elif acao == 'rejeitar':
#         # Lógica para rejeitar a solicitação
#         pass

#     # Gerar PDF após a ação
#     gerar_pdf(solicitacao, steward)

#     # Redirecionar para a página de solicitações
#     redirect_url = request.url_for('pagina_solicitacoes')
#     return RedirectResponse(redirect_url, status_code=303)

