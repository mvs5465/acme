## Header info ##
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_index():
  return render_template('index.html', title='ACME', status='in progress')

@app.route('/programmer')
def programmer():
  return render_template('index.html', title='Programmer', content='programmer.html')

@app.route('/designer')
def designer():
  return render_template('index.html', title='Designer', content='designer.html')
