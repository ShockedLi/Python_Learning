from msilib.schema import ODBCDataSource


def lookupMaxMin(args):
    if len(args) == 0:
        return

    min = args[0]
    max = args[0]

    for num in args[1:len(args)]:
        if num <= min:
            min = num
        elif num >= max:
            max = num
    return min, max

l = [34, 23, 56, 14, 78, 24, 78, 98]

print(lookupMaxMin(l))
