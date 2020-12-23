from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import random


application = Flask(__name__)
application.debug = True    #вывод ошибок в браузер
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///umka.db3'    #Путь/URI базы данных, который будет использоваться для подключения.
#postgresql://scott:tiger@localhost/mydatabase  #для базы Postgres
#mysql://scott:tiger@localhost/mydatabase   #для базы MySQL
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #Если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы. По умолчанию становлен в None, что включает отслеживание но выводит предупреждение, что в будующем будет отчключена по умолчанию. Данная функция требует дополнительную память, и должна быть отключена если не используется.
db = SQLAlchemy(application)


class Klient(db.Model):
    Num = db.Column(db.Integer, primary_key=True)
    Firma = db.Column(db.Text, nullable=True)
    Kont_Litso = db.Column(db.Text, nullable=True)
    Kont_Tel = db.Column(db.Text, nullable=True)
    E_Mail = db.Column(db.Text, nullable=True)
    Adres = db.Column(db.Text, nullable=True)

class Flags(db.Model):
    Num = db.Column(db.Integer, primary_key=True)
    Num_Zakaz = db.Column(db.Integer, nullable = False)
    Opisanie = db.Column(db.Text, nullable=True)
    Kol_vo = db.Column(db.Integer, nullable = False)
    Zena = db.Column(db.Text, nullable = False)
    Data_Out = db.Column(db.Integer, nullable = True)
    Risunok = db.Column(db.Text, nullable=True)

class Zakaz(db.Model):    
    Num = db.Column(db.Integer, primary_key=True)
    Klient = db.Column(db.Text, nullable=True)
    Komment = db.Column(db.Text, nullable=True)
    Data_In = db.Column(db.Integer, nullable = True)
    Data_Out = db.Column(db.Integer, nullable = True)
    Summa = db.Column(db.Text, nullable=True)
    Stage = db.Column(db.Integer, nullable = True)
    Oplata_Inf = db.Column(db.Text, nullable=True)
    Prinjal = db.Column(db.Text, nullable=True)
   

def __repr__(self):
        return self.title



@application.route('/')
def index():
    items = Klient.query.all()
    return render_template('index.html', data=items)

@application.route('/klient')
def klient():
    items = Klient.query.all()
    return render_template('klient.html', data=items)

@application.route('/flags')
def flags():
    items = Flags.query.all()
    return render_template('flags.html', data=items)

@application.route('/zakaz')
def zakaz():
    items = Zakaz.query.all()
    return render_template('zakaz.html', data=items)
    

@application.route('/about')
def about():
    return render_template('about.html')




if __name__ == "__main__":
   application.run(host='0.0.0.0')
