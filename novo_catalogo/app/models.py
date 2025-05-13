from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


# Modelo de Usuário
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    foto_url = Column(String)  # URL da foto do Data Steward ou do solicitante
    papel = Column(String)  # Ex: 'steward', 'solicitante'

    # Relacionamento com solicitações de acesso
    solicitacoes = relationship("SolicitacaoAcesso", back_populates="solicitante")


# Modelo de Tabela (catalogo de dados)
class Tabela(Base):
    __tablename__ = 'tabelas'

    id = Column(Integer, primary_key=True, index=True)
    nome_tabela = Column(String, index=True)
    descricao = Column(Text)  # Descrição da tabela
    dominio = Column(String)  # Ex: 'Financeiro', 'RH'
    data_steward_id = Column(Integer, ForeignKey('usuarios.id'))

    # Relacionamento com o Data Steward (usuário)
    data_steward = relationship("Usuario")

    # Relacionamento com as colunas e solicitações de acesso
    colunas = relationship("Coluna", back_populates="tabela")
    solicitacoes = relationship("SolicitacaoAcesso", back_populates="tabela")


# Modelo de Coluna (campos da tabela)
class Coluna(Base):
    __tablename__ = 'colunas'

    id = Column(Integer, primary_key=True, index=True)
    nome_coluna = Column(String, index=True)
    tipo_dado = Column(String)  # Ex: 'INTEGER', 'VARCHAR'
    descricao = Column(Text)  # Descrição da coluna
    tabela_id = Column(Integer, ForeignKey('tabelas.id'))

    # Relacionamento com a tabela
    tabela = relationship("Tabela", back_populates="colunas")


# Modelo de Solicitação de Acesso
class SolicitacaoAcesso(Base):
    __tablename__ = 'solicitacoes_acesso'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pendente")  # 'pendente', 'aprovado', 'rejeitado'
    solicitante_id = Column(Integer, ForeignKey('usuarios.id'))
    tabela_id = Column(Integer, ForeignKey('tabelas.id'))

    # Relacionamento com os usuários e tabelas
    solicitante = relationship("Usuario", back_populates="solicitacoes")
    tabela = relationship("Tabela", back_populates="solicitacoes")
