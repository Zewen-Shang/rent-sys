from flask import request
import json

from DB import *
from Utils import *


def QueryRentInfo():
    all_attr=("rent_id","user_id","area","price","is_out","min_date","max_date")
    attr_list = []
    data_list=[]
    dbo = DBOpera.DBOpera("root","","se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    for x in all_attr:
        tmp = json_data.get(x)
        if(tmp != None and (x == "min_date" or x == "max_date")):
            tmp = getDateStr.getDateStr(tmp)
        if(tmp != None):
            attr_list.append(x)
            data_list.append(tmp)
    (status,err,res) = dbo.query("rent_info",attr_list,data_list)
    res = list(map(lambda row:(row[0],row[1],row[2],row[3],row[4],{"year":row[5].year,"month":row[5].month,"day":row[5].day}),res))
    return json.dumps({"status":status,"err":err.args[1] if err != None else err,"res":res})