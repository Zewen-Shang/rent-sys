from . import AddRentInfo
from . import DeleteRentInfo
from . import QueryRentInfo
def useRoute(app):
    app.route("/api/rent_info/add",methods=["POST"])(AddRentInfo.AddRentInfo)
    app.route("/api/rent_info/delete",methods=["POST"])(DeleteRentInfo.DeleteRentInfo)
    app.route("/api/rent_info/query",methods=["POST"])(QueryRentInfo.QueryRentInfo)