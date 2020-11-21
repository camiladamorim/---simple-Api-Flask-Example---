#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify,request, Response
from services import *
import json

app=Flask(__name__)

@app.route("/")
def pagPrincipal():
    return(BackParaAPI())


@app.route("/pag2")
def pagReceita():
    return(ReceitaExpandida())


@app.route("/posted",methods=["POST"])
def posted():
    AttDB()
    return Response(status=201)
    #data = request.get_json()
    #name=data['name']
    #howToDo=data['howToDo']
    #return jsonify({"howToDo":howToDo, "name": name})
    #return(json.dumps(data))

    
if __name__=='__main__':
    app.run()



