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
    products = Product.query.all()
    return render_template("index.html", posts=todos_estudos, products=products, title="Bíblia em mim | Home")



@app.route('/post/<int:id>')
def post(id):
    # Procurar o artigo pelo identificador 'post'
    post = Estudos.query.get_or_404(id)
    return render_template("postlayout.html", post=post, title=post.title)


@app.route('/estudos_user')
def estudos_user():
    estudos = Estudos.query.all()
    return render_template('estudos_user.html', estudos=estudos)



@app.route('/cadastro')
def cadastro():
    estudos = Estudos.query.all()
    produtos = Product.query.all()
    return render_template('cadastro.html', estudos=estudos, produtos=produtos)



#CRUD estudos
@app.route('/estudos')
def estudos():
    estudos = Estudos.query.all()
    return render_template("estudos.html", estudos = estudos)


@app.route('/estudos/editar/<int:id>', methods=['POST'])
def editar_estudo(id):
    estudo = Estudos.query.get(id)
    estudo.title = request.form['title']
    estudo.content = request.form['content']
    estudo.resume = request.form['resume']
    estudo.image = request.form['image']

    db.session.add(estudo)
    db.session.commit()
    return redirect(url_for('estudos'))

@app.route('/estudos/novo', methods=['POST'])
def novo_estudo():
    estudo = Estudos(
        title = request.form['title'],
        content = request.form['content'],
        resume = request.form['resume'],
        image = request.form['image']
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




#CRUD Products
@app.route('/products', methods=['GET'])
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)



@app.route('/products/novo', methods=['GET','POST'])
def new_product():
    product = Product(
        name = request.form['name'],
        author = request.form['author'],
        link = request.form['link'],
        category = request.form['category']
    )
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('products'))



@app.route('/products/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.author = request.form['author']
        product.link = request.form['link']
        product.category = request.form['category']

        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))



@app.route('/product/delete/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))




@app.route('/Sobre')
def Sobre():
    return render_template("sobre.html")





if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port = 5153)



