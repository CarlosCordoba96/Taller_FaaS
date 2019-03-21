#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys

def main(dict):
    votos={
        "Ciudad Real": 0,
        "Granada": 0,
        "Teruel": 0,
        "Segovia": 0
    }

    lista=[]
    for i in dict["rows"]:
        opt=i["doc"]["vote"]
        votos[opt]=votos[opt]+1

    for i in votos:
        newdict={}
        newdict["opcion"]=i
        newdict["valor"]= votos[i]
        lista.append(newdict)

    return {"entries":lista}
