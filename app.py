#!/usr/bin/env python

from bottle import Bottle, HTTPError, route, run, static_file, template, post, request
import bottle_mysql
from bottle_log import LoggingPlugin
import os

DBUSER=os.environ.get("DBUSER")
DBPASS=os.environ.get("DBPASS")
DBNAME=os.environ.get("DBNAME")
DBHOST=os.environ.get("DBHOST")
DBPORT=int(os.environ.get("DBPORT"))

app = Bottle()
app.install(LoggingPlugin(app.config))
# plugin = bottle_mysql.Plugin(dbuser='user', dbpass='pass', dbname='db', dbhost='127.0.0.1', dbport=6446)
plugin = bottle_mysql.Plugin(dbuser=DBUSER, dbpass=DBPASS, dbname=DBNAME, dbhost=DBHOST, dbport=DBPORT)
app.install(plugin)

@app.route('/show')
def show(db, logger):
    db.execute('SELECT * FROM user')
    row = db.fetchone()
    if row:
        return row
    return HTTPError(404, "Page not found")

@route('/favicon.ico')
def favicon():
    """Sends the favicon.ico file."""
    return static_file("favicon.ico", root='.')

run(app, host='0.0.0.0', port=8080)
