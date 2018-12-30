# import all the modules we need
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our app
app = Flask(__name__)
#app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

'''
Usually, it is a good idea to load a configuration from a configurable file.
This is what from_envvar() can do, replacing the from_object() line above.
That way someone can set an environment variable called FLASKR_SETTINGS to specify
a config file to be loaded which will then override the default values.
'''

# a method to easily connect to the database specified
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()






if __name__ == '__main__':
    app.run()
