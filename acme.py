from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import sqlite3 as sql


app = Flask(__name__)
app.config.from_object(__name__)

#import models
import views

DATABASE = 'database/database.sqlite'

def connect_db():
    """Connects to the specific database."""
    rv = sql.connect(DATABASE)
    #rv.row_factory = sql.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        
@app.route('/db/all')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT * FROM salaries WHERE JobTitle=\'Transit Operator\';')
    entries = cur.fetchall()
    return render_template('layout.html', content='modules/data.html', status='running', entries=entries)