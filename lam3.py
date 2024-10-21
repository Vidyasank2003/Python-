def f1(fun):
    value=fun(5,6)
    print(value)
f1(lambda num1,num2:num1 if num1>num2 else num2)