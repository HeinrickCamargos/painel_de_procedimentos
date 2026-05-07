from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Bloco(db.Model):
    __tablename__ = 'bloco'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    procedimentos = db.relationship('Procedimento', backref='bloco_pai', lazy=True, cascade="all, delete-orphan")


class Procedimento(db.Model):
    __tablename__ = 'procedimento'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    setor = db.Column(db.String(100))
    descricao = db.Column(db.Text, nullable=False)
    arquivo_path = db.Column(db.String(255))
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    bloco_id = db.Column(db.Integer, db.ForeignKey('bloco.id'), nullable=False)
