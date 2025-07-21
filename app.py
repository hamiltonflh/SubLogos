from flask import Flask, render_template, request, redirect, url_for
from repositories.database import db
from repositories.Estudos import Estudos
from repositories.Product import Product
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


@app.route('/')
def index():
    todos_estudos = Estudos.query.all()
    return render_template("index.html", posts=todos_estudos, title="Bíblia em mim | Home")



@app.route('/post/<int:id>')
def post(id):
    # Procurar o artigo pelo identificador 'post'
    post = Estudos.query.get_or_404(id)
    return render_template("postlayout.html", post=post, title=post.title)


@app.route('/estudos')
def estudos():
    estudos = Estudos.query.all()
    return render_template("estudos.html", estudos = estudos)


@app.route('/estudos/editar/<int:id>', methods=['GET', 'POST'])
def editar_estudos(id):
    estudo = Estudos.query.get(id)
    if request.method == 'POST':
        estudo.title = request.form['title']
        estudo.content = request.form['content']
        estudo.resume = request.form['resume']

        db.session.add(estudo)
        db.session.commit()
    return redirect(url_for('estudos'))

@app.route('/estudos/novo', methods=['GET', 'POST'])
def novo_estudo():
    estudo = Estudos(
        title = request.form['title'],
        content = request.form['content'],
        resume = request.form['resume'],
    )
    db.session.add(estudo)
    db.session.commit()
    return redirect(url_for('estudos'))



@app.route('/estudos/deletar/<int:id>', methods=['GET','POST'])
def delete_estudo(id):
    estudo = Estudos.query.get_or_404(id)
    db.session.delete(estudo)
    db.session.commit()
    return redirect(url_for('estudos'))



@app.route('/store')
def store():
    return render_template("store_index.html")


@app.route('/store/<int:productid>')
def store_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return "Produto não encontrado", 404
    return render_template("store_product", product=product)



@app.route('/Sobre')
def Sobre():
    return render_template("sobre.html")





if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port = 5153)



