from flask import request
import json

from DB import *
from Utils import getHash

def DeleteOrgUserPend():
    dbo = DBOpera.DBOpera("root","","se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    all_attr = ("user_id",)
    attr_list = []
    data_list = []
    for x in all_attr:
        tmp = json_data.get(x)
        if(tmp != None): 
            attr_list.append(x)
            data_list.append(tmp)
    (status,err) = dbo.delete("org_user_pend",attr_list,data_list)
    return json.dumps({"status":status,"err":err.args[1] if err != None else err})  