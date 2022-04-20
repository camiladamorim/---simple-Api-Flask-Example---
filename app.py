#!/usr/bin/env python
# coding: utf-8

from flask import Flask,jsonify,request, Response
# import services
import json

app=Flask(__name__)

@app.route("/")
def main_page():
    with open("receitas.json", "r") as read_file:
        meuObj = json.load(read_file)
    meuJSON=json.dumps(meuObj)
    return(meuJSON)


@app.route("/pag2")
def recipe_page():
    with open("receitas.json", "r") as read_file:
        meuObj = json.load(read_file)
    meuJSON=json.dumps(meuObj)
    return("meuJSON")


@app.route("/posted",methods=["POST"])
def posted():
    data = request.get_json()
    with open("receitas.json", "w") as write_file:
        json.dump(data,write_file)
    #data = request.get_json()
    #name=data['name']
    #howToDo=data['howToDo']
    #return jsonify({"howToDo":howToDo, "name": name})
    #return(json.dumps(data))

    
if __name__=='__main__':
    app.run()



