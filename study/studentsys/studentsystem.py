# author : comma
# date : 2020/11/9 15:09
import os

from study.字符串的操作 import lst

filename = 'student.txt'


def mian():
    while True:
        menum()
        choice = int(input('请选择'))
        if choice in range(8):
            if choice == 0:
                answer = input('确定要退出系统吗？ y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢你的使用！')
                    break
                else:
                    continue
            if choice == 1:
                insert()
            if choice == 2:
                search()
            if choice == 3:
                delete()
            if choice == 4:
                update()
            if choice == 5:
                sort()
            if choice == 6:
                total()
            if choice == 7:
                show()


def menum():
    print('=================学生信息管理系统================')
    print('---------------------功能菜单-------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.对学生信息排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('----------------------------------------------')


'''
添加学生信息：
1.定义一个学生列表接收学生信息，单个学生信息以字典方式储存
'''


def insert():
    student_lst = []
    while True:
        stuid = input('请输入学号（如：1001）：')
        if not stuid:
            break
        name = input('请输入学生姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
        student = {'id': stuid, 'name': name, 'english': english, 'python': python, 'java': java}
        student_lst.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 调用save方法保存数据
    save2(student_lst)


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='UTF-8')
        print('追加方式保存1')
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')
        print('覆盖方式保存1')

    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def save2(lst2):
    try:
        with open(filename, 'a', encoding='UTF-8') as stu_txt2:
            for item in lst2:
                stu_txt2.write(str(item) + '\n')
        print('以追加方式添加')
    except:
        with open(filename, 'a', encoding='UTF-8') as stu_txt2:
            for item in lst2:
                stu_txt2.write(str(item) + '\n')
        print('以覆盖方式添加')


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您输入的信息有误，请重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                students = rfile.readlines()
                for item in students:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否继续查询？y/n')
            if answer == 'y':
                continue
            else:
                break


def show_student(lst):
    if len(lst) == 0:
        print('没有查到学生信息')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'  # {:^8}---:前面标识占位符（省略了），^标识左右对齐，8标识宽度
    print(format(format_title.format('id', '姓名', '英语成绩', 'python成绩', 'Java成绩', '总成绩')))
    format_content = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_content.format(item.get('id'), item.get('name'), item.get('english'), item.get('python'),
                                    item.get('java'),
                                    int(item.get('english')) + int(item.get('python') + int(item.get('java')))))


def delete():
    while True:
        student_id = input('请输入要删除的学生ID')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()  # 读取文件到列表中
            else:
                student_old = []  # 如果文件为空，则给列表赋一个空值
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:  # 判断这个元素的id和要删除的id是否一样，不一样就继续存储到文件中，不一样的时候flag标记为True，不写入文件（即：删除）
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生')
        else:
            print('无学生信息')
            break
        show()
        answer = input('是否继续删除？y/n')
        if answer == 'y':
            continue
        else:
            break


def sort():
    if os.path.exists(filename):
        stulist = []
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                d = dict(eval(item))
                stulist.append(d)
        asc_or_desc = input('请选择（0.升序，1.降序）')
        if asc_or_desc == '0':
            asc_or_desc = False
        elif asc_or_desc == '1':
            asc_or_desc = True
        else:
            print('输入有误，请重新输入')
            sort()
        mode = input('请选择排序方式：1-按英语成绩排序，2-按python成绩排序，3-按Java成绩排序，0-按总成绩排序')
        if mode == '1':
            stulist.sort(key=lambda x: int(x['english']), reverse=asc_or_desc)
        elif mode == '2':
            stulist.sort(key=lambda x: int(x['python']), reverse=asc_or_desc)
        elif mode == '3':
            stulist.sort(key=lambda x: int(x['java']), reverse=asc_or_desc)
        else:
            stulist.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc)
        show_student(stulist)
    else:
        print('暂未保存文件')


def update():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入学生id：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息了，可以修改！')
                while True:
                    try:
                        d['name'] = input('请输入学生姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['java'] = input('请输入java成绩：')
                        d['python'] = input('请输入python成绩：')
                    except:
                        print('输入信息有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('信息修改成功！')
            else:
                wfile.write(str(d) + '\n')
    answer = input('是否继续修改其它学生信息？y/n:')
    if answer == 'y':
        update()


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有名{len(students)}学生')
            else:
                print('还未录入学生信息')
    else:
        print('暂未保存数据信息')


def show():
    if os.path.exists(filename):
        stulist = []
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                d = dict(eval(item))
                stulist.append(d)
        if stulist:
            show_student(stulist)
        else:
            print('您还未录入学生信息')
    else:
        print('暂未保存数据信息')


if __name__ == '__main__':
    mian()
