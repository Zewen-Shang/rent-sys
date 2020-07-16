from . import RentInfo
from . import ComUser
from . import OrgUser
from . import OrgUserPend
def useRoute(app):
    RentInfo.useRoute(app)
    ComUser.useRoute(app)
    OrgUser.useRoute(app)
    OrgUserPend.useRoute(app)