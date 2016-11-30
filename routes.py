from flask import Flask, render_template, request
from acme import app, get_db

print "Opened routes.py"

@app.route('/')
def show_index():
  return render_template('layout.html', title='ACME', status='good')

@app.route('/programmer')
def programmer():
  return render_template('layout.html', title='Programmer', content='programmer.html', status='good')

@app.route('/designer')
def designer():
  return render_template('layout.html', title='Designer', content='modules/designer.html', status='good')

@app.route('/hacker')
def hacker():
    ipaddr=request.remote_addr
    routes=request.access_route
    return render_template('layout.html', title='Hacker', content='modules/hacker.html', status='bad', ipaddr=ipaddr, routes=routes)

@app.route('/database')
def database():
    entries = []
    entries.append("<<no entries yet>>")
    return render_template('layout.html', title='Database', content='modules/data.html', status='good', entries=entries)

@app.route('/db/all')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT * FROM salaries LIMIT 100;')
    entries = cur.fetchall()
    return render_template('layout.html', content='modules/data.html', status='running', entries=entries)

@app.route('/db/custom')
def custom_query():
    entries = []
    query = request.args['query_str']
    db = get_db()
    cur = db.execute(query)
    entries = cur.fetchall()
    keys = cur.description
    return render_template('layout.html', title='Database', content='modules/data.html', status='good', entries=entries, query=query, keys=keys)

@app.route('/db/builder')
def build_query():
    
    # Define variables
    query = ""
    entries = []
    keys = []
    
    # Extract query info from GET request
    columns = request.args.getlist('fields')
    years = request.args.getlist('years')
    
    # Construct query
    query = "SELECT " + columns[0] + " FROM salaries LIMIT 100;"
    
    # Execute query
    db = get_db()
    cur = db.execute(query)
    entries = cur.fetchall()
    keys = cur.description
    
    # Return template along with variables
    return render_template('layout.html', title='Database', content='modules/data.html', status='good', entries=entries, query=query, keys=keys)