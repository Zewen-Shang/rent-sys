from . import AddOrgUser
# from . import DeleteRentInfo
from . import QueryOrgUser
def useRoute(app):
    app.route("/api/org_user/add",methods=["POST"])(AddOrgUser.AddOrgUser)
    # app.route("/api/rent_info/delete",methods=["POST"])(DeleteRentInfo.DeleteRentInfo)
    app.route("/api/org_user/query",methods=["POST"])(QueryOrgUser.QueryOrgUser)