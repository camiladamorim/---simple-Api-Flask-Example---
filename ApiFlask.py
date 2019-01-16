#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify,request
from services import *

app=Flask(__name__)

@app.route("/")
def pagPrincipal():
    return(BackParaAPI())


@app.route("/pag2")
def pagReceita():
    return(ReceitaExpandida())


@app.route("/posted",methods=["POST"])
def posted():
    data = request.get_json()
    name=data['name']
    howToDo=data['howToDo']
    return jsonify({"howToDo":howToDo, "name": name})

    
if __name__=='__main__':
    app.run()



