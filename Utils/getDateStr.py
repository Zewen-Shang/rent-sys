def getDateStr(date):
    if(date == None):
        return date
    return "%s-%s-%s" %(date["year"],date["month"],date["day"])