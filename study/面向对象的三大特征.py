# @Author  :  comma 
# @Date    :  2020-11-03 08:00


'''
面向对象的三大特征：
封装：提高程序的安全性
     将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象外部调用方法。这样，无序关心方法内部的具体实现细节，从而隔离了复杂度。
     在Python中没有专门修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个"_"

'''


class Comma(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有化属性，外部不可以使用

    def show(self):
        print(self.name, self.__age)


com = Comma('逗号', 30)
com.show()
print(com.name)  # 在类的外部使用类属性
# print(com.__age)  # 私有化的属性，外部不能使用

# print(dir(com))
print(com._Comma__age)  # 在类的外部可以通过 _类名__类属性 的方式进行访问私有变量
print('---------------------------')


#################### 继承 ################
class Stone(Comma):
    def __init__(self, name, age, gender):
        super(Stone, self).__init__(name, age)
        self.gender = gender

    def show(self):  # 重写show方法
        super(Stone, self).show()  # 继承父类的show方法
        print(self.gender)  # 增加自己特有的处理


stone = Stone('石头', 28, '男')  # 创建子类Stone的实例方法
stone.show()  # 子类继承了父类的方法show()

# 多继承
class sun(Comma,Stone): # sun同时继承了Comma和Stone，继承这两个类的所有对象方法
    pass


############## 方法重写 ###############
"""
如果子类对继承自父类的某个属性或者方法不满意，可以在子类中对其（方法体）进行重新编写
子类重写丰厚的方法中可以通过super().xxx()调用父类中被重新的方法
"""
