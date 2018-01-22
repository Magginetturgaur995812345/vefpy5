from bottle import *
import os

@route("/")
def index():
        return '<a href="sida1">sida1</a>:''<a href="sida2">sida2</a>:''<a href="sida3">sida3</a>:'
@route("/sida1")
def index():
	return "<b>Þetta er síða 1</b>"
@route("/sida2")
def index():
	return "<b>Þetta er síða 2</b>"
@route("/sida3")
def index():
	return "<b>Þetta er síða 3</b>"

run(host="0.0.0.0", port=os.enviorn.get('PORT'))
#run(host="localhost", port=8080)
