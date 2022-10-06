# from msilib.schema import ODBCDataSource


# def lookupMaxMin(args):
#     if len(args) == 0:
#         return

#     min = args[0]
#     max = args[0]

#     for num in args[1:len(args)]:
#         if num <= min:
#             min = num
#         elif num >= max:
#             max = num
#     return min, max

# l = [34, 23, 56, 14, 78, 24, 78, 98]

# print(lookupMaxMin(l))

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n+ 1
# #执行
# for n in fab(5):
#     print(n)

# def f1():
#     print(1/0)

# def f2():
#     f1()

# def f3():
#     f2()

# f3()
 
from re import A


# #a = 1
# def outer():
#     a = 10 
#     def inner():
#         nonlocal a
#         #global a
#         a += 1
#         print(a)
#     return inner

# outer_result = outer()
# outer_result()
# outer_result()



# print(id)

def log(func):
    def wrapper(*args, **kwargs):
        print('调用的函数名为%s' % func.__name__)
        print('args=%s,kwargs=%s' % (args,kwargs))
        return func(*args,**kwargs)
    return wrapper
 


@log
def add(a,b):
    return a+b


result = add(1,2)
print(result)