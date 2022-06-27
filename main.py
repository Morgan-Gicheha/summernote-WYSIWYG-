 

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
# SQLALCHEMY_DATABASE_URI = "sqlite:///restx.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"



class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    htmlData = db.Column(db.String())

@app.before_first_request
def create():
    db.create_all()



@app.route('/', methods=["POST","GET"])
def index():
    if request.method =="POST":
        data = request.form.get("editordata")
        print(data)
        insertion = Data(htmlData =data )
        db.session.add(insertion)
        db.session.commit()
    mydata = Data.query.all()
    print(mydata)
    return render_template('index.html',mydata=mydata)


 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)