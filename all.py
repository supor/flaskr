from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
from matplotlib.pyplot import title
from sqlalchemy import create_engine, Table, text
from flask.ext.sqlalchemy import SQLAlchemy
from markdown import Markdown
# configuration
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://root:@localhost:3306/blog')
DATABASE = 'mysql://root:@localhost:3306/blog'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

markdown = Markdown()
db = SQLAlchemy()

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


class Article2(db.Model):
    __tablename__ = 'entries2'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    text = db.Column(db.String(20), unique=True)

    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text

DBSession = sessionmaker(bind=engine)
# article = Table('entries', DBSession, autoload=True)

article = Article2(id='7', title='hello', text='hello python+flask')
db.session.add(article)
db.session.commit(article)


if __name__ == '__main__':
    app.run()
