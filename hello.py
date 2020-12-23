from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import random


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    

def __repr__(self):
        return self.title



@application.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', data=items)


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/buy/<int:id>')
def item_buy(id):
    return str(id)


@application.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']

        item = Item(title=title, price=price)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Получилась ошибка"
    else:
        return render_template('create.html')


@application.route("/1")
def hello():
	return "<h1 style='color:blue'>Привет, Мир!</h1>"   


@application.route("/2")
def hell():
	movies = ["Добрый день", "Привет", "Пока", "Добрый вечер", "Назад"]
	return "<h1 style='color:blue'>" + random.choice(movies) + "</h1>"


if __name__ == "__main__":
   application.run(host='0.0.0.0' debug=True)
