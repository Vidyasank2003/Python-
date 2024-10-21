def upper_decorator(fun):
    def inner(a,b):
        c,d=fun(a,b)
        cancat=c.upper()+' '+ d.upper()
        return cancat
    return inner

@upper_decorator
def str_fun(x,y):
    return x,y
a=str_fun("hello gm","palle")
print(a)
