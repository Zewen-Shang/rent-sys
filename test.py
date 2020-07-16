from functools import reduce
def fun(x,y):
    return str(x) + ",'%s'" % y

a = (1,2,3,4,5)
print('\'' + reduce(fun,a))