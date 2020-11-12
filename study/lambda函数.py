# @Author  :  comma 
# @Date    :  2020-11-12 23:17

'''
一个语法
在Python中，lambda的语法是唯一的。其形式如下：

lambda argument_list: expression

其中，lambda是Python预留的关键字，argument_list和expression由用户自定义。具体介绍如下。

1. 这里的argument_list是参数列表，它的结构与Python中函数(function)的参数列表是一样的。具体来说，argument_list可以有非常多的形式。例如：

    a, b
    a=1, b=2
    *args
    **kwargs
    a, b=1, *args
    空
    ......
2. 这里的expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的。以下都是合法的表达式：

    1
    None
    a + b
    sum(a)
    1 if a >10 else 0
    ......

3.  这里的lambda argument_list: expression表示的是一个函数。这个函数叫做lambda函数。



三个特性

lambda函数有如下特性：

lambda函数是匿名的：所谓匿名函数，通俗地说就是没有名字的函数。lambda函数没有名字。

lambda函数有输入和输出：输入是传入到参数列表argument_list的值，输出是根据表达式expression计算得到的值。

lambda函数一般功能简单：单行expression决定了lambda函数不可能完成复杂的逻辑，只能完成非常简单的功能。由于其实现的功能一目了然，甚至不需要专门的名字来说明。

下面是一些lambda函数示例：

     lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
     lambda:None；函数没有输入参数，输出是None
     lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
     lambda **kwargs: 1；输入是任意键值对参数，输出是1


四个用法:


    1.由于lambda语法是固定的，其本质上只有一种用法，那就是定义一个lambda函数。在实际中，根据这个lambda函数应用场景的不同，可以将lambda函数的用法扩展为以下几种：

将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。

例如，执行语句add=lambda x, y: x+y，定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1,2)，输出为3。

    2.将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。

例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用：time.sleep=lambda x:None。这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做。

    3. 将lambda函数作为其他函数的返回值，返回给调用者。

函数的返回值也可以是函数。例如return lambda x, y: x+y返回一个加法函数。这时，lambda函数实际上是定义在某个函数内部的函数，称之为嵌套函数，或者内部函数。对应的，将包含嵌套函数的函数称之为外部函数。内部函数能够访问外部函数的局部变量，这个特性是闭包(Closure)编程的基础，在这里我们不展开。

    4. 将lambda函数作为参数传递给其他函数。

部分Python内置函数接收函数作为参数。典型的此类内置函数有这些。

    ①filter函数。此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。

    ②sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。

map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，其结果[2, 3, 4]。

    ③reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。

另外，部分Python库函数也接收函数作为参数，例如gevent的spawn函数。此时，lambda函数也能够作为参数传入。

'''

a = [{'id': 10}, {'id': 30}, {'id': 13}]  # 定义一个列表，列表中的元素是字典的形式，这个列表就是一个可迭代对象
a.sort(key=lambda x: int(x['id']))  # sort函数排序是按元素排序的，a的元素是一个个字典（那么x迭代的就是字典），然后将字典元素转换成int类型进行比较
print(a)

'''
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
'''

# filter过滤器，一个函数，一个可迭代对象，返回值是一个迭代器，如果要使用输出，需要转换类型
c = list(filter(lambda x: int(x['id']) > 20, a))  # a是一个可迭代对象，迭代a中的元素，由于a中的元素是字典，，所以取值来比较
print(c)
