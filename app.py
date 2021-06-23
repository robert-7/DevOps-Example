import os

import bottle_mysql
from bottle import Bottle
from bottle import HTTPError
from bottle import run
from bottle import static_file

DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")
DBHOST = os.environ.get("DBHOST")
DBPORT = int(os.environ.get("DBPORT"))

app = Bottle()
plugin = bottle_mysql.Plugin(
    # overwrite with this for a local setup:
    # dbuser="user", dbpass="pass", dbname="db",
    #   dbhost="127.0.0.1", dbport=6446
    dbuser=DBUSER,
    dbpass=DBPASS,
    dbname=DBNAME,
    dbhost=DBHOST,
    dbport=DBPORT,
)
app.install(plugin)


@app.route("/show")
def show(db):
    db.execute("SELECT * FROM user")
    row = db.fetchone()
    if row:
        return row
    return HTTPError(404, "Page not found")


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon.ico file."""
    return static_file("favicon.ico", root=".")


run(app, host="0.0.0.0", port=8080)
