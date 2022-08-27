

from cgi import print_exception
from ctypes.wintypes import WORD


print(ord('A'))
print(chr(65))

L = list(["python",12,"a"])
print("python" is L)

L = list(range(10))
print(L*2)


book  = "《图解Python教程》"
price = 68.88
word  = "我花了%7.3f,买了一本名为%s的书" % (price, book)
print(word)

from datetime import datetime
print(format(datetime(2000,3,21,23,23,23),'%Y-%m-%d %H:%M:%S'))