from sqlalchemy import create_engine
from run import app
from flask import g


def connect_db():
    return create_engine(app.config("DATABASE"))


@app.before_request
def before_request():
    g.db = connect_db()
    return g.db


@app.teardown_request
def teardown_request(exception=None):
    # db = before_request()
    g.db.close()
