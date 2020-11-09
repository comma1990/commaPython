# author : comma
# date : 2020/11/9 15:09

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
    print('\t\t\t\t\t\t8.退出系统')
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
    save(student_lst)


def save(lst):
    try:
        with open(filename, 'a', encoding='UTF-8') as stu_txt:
            for item in lst:
                stu_txt.write(item + '\n')


    except:
        with open(filename, 'w', encoding='UTF-8') as stu_txt:
            for item in lst:
                stu_txt.write(str(item).replace('{', '').replace('}', '') + '\n')


def search():
    pass


def delete():
    pass


def sort():
    pass


def update():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    mian()
