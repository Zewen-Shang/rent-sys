from flask import Flask
from Api import *

app = Flask(__name__,template_folder="templates",static_folder="static")

useRoute(app)

# app.route("/api",methods=["POST"])(AddRentInfo.AddRentInfo)

# app.route("/api/delete_rent_info",methods=["POST"])(DeleteRentInfo.DeleteRentInfo)
# dbo = DataBaseOpera("root","dhy2bdhy2b","SE_Project") 
# dbo.insert("rent_info",("12345","1","hubei",5222))
# print(dbo.query("rent_info",("id",),("12345",)))