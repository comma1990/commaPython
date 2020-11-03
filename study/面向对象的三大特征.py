# @Author  :  comma 
# @Date    :  2020-11-03 08:00


'''
面向对象的三大特征：
封装：提高程序的安全性
     将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象外部调用方法。这样，无序关心方法内部的具体实现细节，从而隔离了复杂度。
     在Python中没有专门修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个"_"

'''

class Comma:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # 私有化属性，外部不可以使用
    def show(self):
        print(self.name,self.__age)


com=Comma('逗号',30)
com.show()
print(com.name) #在类的外部使用类属性
# print(com.__age)  # 私有化的属性，外部不能使用

# print(dir(com))
print(com._Comma__age)  # 在类的外部可以通过 _类名__类属性 的方式进行访问私有变量