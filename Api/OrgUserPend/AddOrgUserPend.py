from flask import request
import json


from DB import *
from Utils import getHash

def AddOrgUserPend():
    dbo = DBOpera.DBOpera("root","","se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    all_attr = ("user_name","represent","password")
    attr_list = ["user_id"]
    data_list = [getHash.getHash(json_data)]
    for x in all_attr:
        tmp = json_data.get(x)
        if(tmp != None): 
            attr_list.append(x)
            data_list.append(tmp)
    (status,err) = dbo.insert("org_user_pend",data_list)
    return json.dumps({"status":status,"err":err.args[1] if err != None else err})  