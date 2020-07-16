from . import AddOrgUserPend
from . import DeleteOrgUserPend
from . import QueryOrgUserPend
def useRoute(app):
    app.route("/api/org_user_pend/add",methods=["POST"])(AddOrgUserPend.AddOrgUserPend)
    app.route("/api/org_user_pend/delete",methods=["POST"])(DeleteOrgUserPend.DeleteOrgUserPend)
    app.route("/api/org_user_pend/query",methods=["POST"])(QueryOrgUserPend.QueryOrgUserPend)