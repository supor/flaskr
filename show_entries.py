# -*-coding:utf-8 -*-

from flask import render_template, session, abort, request, flash, redirect, url_for
from run import app
from create_db import Article
from connect_db import before_request


@app.route('/')
def show_entries():
    article = Article('id', 'title', 'text')
    db = before_request()
    cur = db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    from create_db import engine,article
    if not session.get('logged_in'):
        abort(401)
    con = engine.connect()
    con.execute(article.insert(id=5, title='python', text='flask'))
    con.execute('select * from users where id = :1', [1]).first()
    engine.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
