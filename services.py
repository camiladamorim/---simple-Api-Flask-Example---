

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

