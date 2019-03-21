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
from cloudant.client import Cloudant
user=
password=
urll=
#DATOS CENSURADOS YA QUE SON SENSIBLES PARA TENERLOS DESCUBIERTOS EN EL REPOSITORIO

def main(dict):
    client = Cloudant(user, password, url=urll,  connect=True, auto_renew=True)
    my_database = client['datos']

    my_dict=dict["doc"]
    my_id=my_dict["_id"]


    if my_id in my_database:
        my_document=my_database[my_id]
        my_document["vote"]=my_dict["vote"]
        my_document["createdAt"]=my_dict["createdAt"]
        my_document.save()

    else:
        my_database.create_document(my_dict)
    print(my_dict)
    return { 'message': 'Hello world' }
