from functools import reduce

def listToString(li):
    return '\'' + reduce(lambda x,y : str(x) + "','%s" % y , li) + "\'"

def twoListToCond(list1,list2):
    ans = []
    i = 0
    while(i < list1.__len__()):
        ans.append([list1[i],list2[i]])
        i = i+1
    return reduce(
        lambda x,y : x + ' AND ' + y,
        map(
            lambda x : 
                x[0][4:] + '>=' + "'%s'"%x[1] if x[0].startswith("min") else  x[0][4:] + '<=' + "'%s'"%x[1] if x[0].startswith("max") else x[0] + '=' + "'%s'"%x[1],
            ans
        )
    )