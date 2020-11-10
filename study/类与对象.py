# @Author  :  comma 
# @Date    :  2020-11-02 21:47


class Student:  # 类名以大写字母开头
    native_place = '海州'  # 方法外定义的变量称之为类属性

    def __init__(self, name, age):  # 初始化方法
        self.name = name  # self.name 称为实体属性，然后将方法中定义的局部变量name的赋值给了它。
        self.age = age

    @staticmethod  # 静态方法
    def staticFun():  # 静态方法不能有参数
        print('我是一个静态方法，因为我是@staticmethod修饰的')

    @classmethod  # 类方法
    def classmd(cls, args):  # 类方法中默认添加一个cls参数，还可以自己添加参数args，类方法可以直接通过类名.方法名 调用
        print('我是一个类方法，因为我是@classmethod修饰的', args)

    def function(self, nikename):  # self自动添加，默认就有，代表类本身
        print(nikename)


# 创建类的实例化对象
stu1 = Student('土豆', 13)  # 因为类的初始化方法定义了两个参数，所以创建类对象的时候必须传两个参数
stu1.gender = '男'  # 为对象stu1创建变量，只在stu1这个对象中可用，Student创建的其它对象不可以用
print(stu1.name, stu1.gender)
stu1.function('憨憨')  # 对象名.方法名(参数)
stu1.staticFun()
stu1.classmd('测试参数')
print('-----------下面是方法的另一种调用方式--------------')
Student.function(stu1, '渣渣')  # 类方法调用的另种方式，类名.方法(实例化对象，参数)  --->实际上实例化对象就是方法定义出的self
print('-----------------------')

print(stu1.native_place)
Student.native_place = '连云港'  # 类的属性重新赋值后，内存中的值变化了
print(stu1.native_place)

print('--------类方法的使用方式------------')
Student.classmd('args参数')  # 直接通过 类名.类方法名 使用，不需要实例化对象

print('-----------静态方法的使用------------')
Student.staticFun()  # 直接通过 类名.方法名 调用，不需要实例化方法


# 定在类之外的函数，并赋值给对象方法
def show():
    print("定义在类之外的，称为函数")


stu1.show = show    # 次数函数后面不能加括号（）
stu1.show()
