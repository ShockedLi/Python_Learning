

# class function(object):

    

#     def __init__(self,age,name) -> None:
#         self.age = age
#         self.name = name
#     @staticmethod  
#     def sayHi():
#         print("你好啊")

#     def sayHello(self):
#         self.sayHi()
#         print("我是%s,今年%d岁了" % (self.name, self.age))

#     pass


# f = function(112, "厉振汉")
# f.sayHi()
# f.sayHello()

# print(dir(f))

# print('-----------------------------------')

# print(function.__dict__)
# print(f.__dict__)

class MyClass(object):

    def __init__(self) -> None:
        self.data = 0
        pass

    def __iter__(self):
        return self
        pass

    def __next__(self):
        if self.data < 5:
            self.data += 1
            return self.data
        else:
            raise StopIteration() 


for i in MyClass():
    print(i)