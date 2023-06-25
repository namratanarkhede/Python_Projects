
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import sqlite3
from sqlalchemy.orm import relationship



class infoForm(FlaskForm):
    YourName = StringField("First Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    mobileno = StringField("Mobile No", validators=[DataRequired(), Length(min=10, max=10)])
    vechicleno = StringField("Vechicle No", validators=[DataRequired()])
    whattorepair = StringField("What to repair?", validators=[DataRequired()])
    submit = SubmitField("Send Message")


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "abcd"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class infoform(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    YourName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mobileno = db.Column(db.String(15))
    vechicleno = db.Column(db.String(15))
    whattorepair = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/knowmore")
def knowmore():
    return render_template('knowmore.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
