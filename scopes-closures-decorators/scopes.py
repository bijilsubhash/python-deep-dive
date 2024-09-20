a = 10

print("Value of a before func:", a)

def func():
    a = 20
    print("Value of a in func and before inner_func:", a)
    def inner_func():
        nonlocal a
        a = 30
        print("Value of a in inner_func:", a)
    inner_func()
    print("Value of a in func and after inner_func:", a)
    pass

func()
print("Value of a outside func :", a)
