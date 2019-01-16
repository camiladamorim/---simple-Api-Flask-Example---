

def BackParaAPI():
    import json
    with open("receitas.json", "r") as read_file:
        meuObj = json.load(read_file)
    #meuObj = {'tuplas': [[1,2],[3,5],[7,2],[8,0]]}
    meuJSON=json.dumps(meuObj)
    return(meuJSON)


def ReceitaExpandida():
    import json
    with open("receitas.json", "r") as read_file:
        meuObj = json.load(read_file)
    meuJSON=json.dumps(meuObj)
    return("meuJSON")


def AttDB():
    import json
    from flask import request
    data = request.get_json()
    with open("receitas.json", "w") as write_file:
        json.dump(data,write_file)
    #name=data['name']
    #howToDo=data['howToDo']
    #return jsonify({"howToDo":howToDo, "name": name})
    #return(json.dumps(data))

