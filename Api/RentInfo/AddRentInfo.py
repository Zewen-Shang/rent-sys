from flask import request
import json


from DB import *
from Utils import getHash

def AddRentInfo():
    dbo = DBOpera.DBOpera("root","","se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    rent_id = getHash.getHash((json_data))
    user_id = json_data.get("user_id")
    area = json_data.get("area")
    price = json_data.get("price")
    is_out = json_data.get("is_out")
    date_obj = json_data.get("date")
    date = "%s-%s-%s"%(date_obj["year"],date_obj["month"],date_obj["day"])
    (status,err) = dbo.insert("rent_info",(rent_id,user_id,area,price,is_out,date))
    return json.dumps({"status":status,"err":err.args[1] if err != None else err})  