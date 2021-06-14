#!/usr/bin/env python
import os
from bottle import route, run, static_file, template, post, request

counter = 0

@route("/log", method="POST")
def log():
    """
    Given a string s and an int counter, return the number of 'ERROR' substrings we've seen
    since the app started running.
    """
    global counter
    body = request.body.read().decode("utf-8")
    find_string = "ERROR"
    counter += body.count(find_string)
    return "{{ERROR : {}}}".format(counter)

@route('/favicon.ico')
def favicon():
    """Sends the favicon.ico file."""
    return static_file("favicon.ico", root='.')

run(host='localhost', port=8080)
