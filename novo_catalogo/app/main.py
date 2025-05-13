from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import catalog, users, requests

app = FastAPI()

# Arquivos estáticos (fotos, CSS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Registra os templates do Jinja2
templates = Jinja2Templates(directory="templates")

# Inclui os módulos de rotas
app.include_router(users.router, prefix="")
app.include_router(catalog.router, prefix="/catalogo")
app.include_router(requests.router, prefix="/solicitacoes")
