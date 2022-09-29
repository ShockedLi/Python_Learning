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

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n+ 1
#执行
for n in fab(5):
    print(n)