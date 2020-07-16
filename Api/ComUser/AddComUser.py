from flask import request
import json


from DB import *
from Utils import getHash

def AddComUser():
    dbo = DBOpera.DBOpera("root","","se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    all_attr = ("user_name","password")
    attr_list = ["user_id"]
    data_list = [getHash.getHash(json_data)]
    for x in all_attr:
        tmp = json_data.get(x)
        if(tmp != None): 
            attr_list.append(x)
            data_list.append(tmp)
    (status,err) = dbo.insert("com_user",data_list)
    return json.dumps({"status":status,"err":err.args[0] if err != None else err})  