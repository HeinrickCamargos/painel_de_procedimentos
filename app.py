from flask import Flask, render_template, request, redirect, url_for
from models import db, Bloco, Procedimento
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configurações de Upload
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configurações do Banco de Dados
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ------------- ROTAS ---------------

@app.route('/')
def index():
    busca = request.args.get('busca')
    if busca:
        resultados = Procedimento.query.filter(Procedimento.titulo.contains(busca)).all()
        return render_template('index.html', procedimentos=resultados, busca=busca)
    # Agora buscamos blocos em vez de usuários
    blocos = Bloco.query.all()
    return render_template('index.html', blocos=blocos, busca=None)


@app.route('/bloco/<int:id>')
def ver_bloco(id):
    bloco = Bloco.query.get_or_404(id)
    return render_template('bloco.html', bloco=bloco)


@app.route('/novo_bloco', methods=['GET', 'POST'])
def novo_bloco():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        novo = Bloco(titulo=titulo)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('novo_bloco.html')


@app.route('/novo_procedimento/<int:bloco_id>', methods=['GET', 'POST'])
def novo_procedimento(bloco_id):
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        setor = request.form.get('setor')
        descricao = request.form.get('descricao')
        arquivo = request.files.get('arquivo')

        nome_arquivo = None
        if arquivo and arquivo.filename != '':
            nome_arquivo = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))

        procedimento = Procedimento(
            titulo=titulo,
            setor=setor,
            descricao=descricao,
            bloco_id=bloco_id,
            arquivo_path=nome_arquivo
        )
        db.session.add(procedimento)
        db.session.commit()
        return redirect(url_for('ver_bloco', id=bloco_id))
    return render_template('novo_procedimento.html', bloco_id=bloco_id)


@app.route('/procedimento/<int:id>', methods=['GET', 'POST'])
def detalhe_procedimento(id):
    procedimento = Procedimento.query.get_or_404(id)
    if request.method == 'POST':
        procedimento.titulo = request.form.get('titulo')
        procedimento.descricao = request.form.get('descricao')

        arquivo = request.files.get('arquivo')
        if arquivo and arquivo.filename != '':
            nome_arquivo = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))
            procedimento.arquivo_path = nome_arquivo

        db.session.commit()
        return redirect(url_for('ver_bloco', id=procedimento.bloco_id))
    return render_template('detalhe_procedimento.html', procedimento=procedimento)


@app.route('/deletar_bloco/<int:id>', methods=['POST'])
def deletar_bloco(id):
    bloco = Bloco.query.get_or_404(id)
    db.session.delete(bloco)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/deletar_procedimento/<int:id>', methods=['POST'])
def deletar_procedimento(id):
    proc = Procedimento.query.get_or_404(id)
    b_id = proc.bloco_id
    db.session.delete(proc)
    db.session.commit()
    return redirect(url_for('ver_bloco', id=b_id))


if __name__ == "__main__":
    app.run(debug=True)
