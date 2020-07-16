from flask import request
import json


from DB import *
from Utils import getHash

def DeleteRentInfo():
    dbo = DBOpera.DBOpera("root","","se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    rent_id = json_data.get("rent_id")
    (status,err) = dbo.delete("rent_info",("rent_id",),(rent_id,))
    return json.dumps({"status":status,"err":err.args[1] if err != None else err})