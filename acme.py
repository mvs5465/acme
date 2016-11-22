## Header info ##
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_index():
  return render_template('layout.html', title='ACME', status='good')

@app.route('/programmer')
def programmer():
  return render_template('layout.html', title='Programmer', content='programmer.html', status='good')

@app.route('/designer')
def designer():
  return render_template('layout.html', title='Designer', content='designer.html', status='good')

@app.route('/hacker')
def hacker():
    ipaddr=request.remote_addr
    routes=request.access_route
    return render_template('layout.html', title='Hacker', content='modules/hacker.html', status='bad', ipaddr=ipaddr, routes=routes)

    
