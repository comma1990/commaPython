# author : comma
# date : 2021/1/5 15:57
'''
修改后缀名
修改文件名称
'''
import os


def filerename():
    file_list = os.listdir(r'D:\素材\full')  # 返回path指定的文件夹包含的文件或文件夹的名字的列表。
    currentpath = os.getcwd()  # 获取当前的工作目录
    os.chdir(r'D:\素材\full')  # 必须要吧当前工作目录切换到要修改文件的目录，否则会报错提示找不到文件
    for index, name in enumerate(file_list):
        # print(name)
        if not os.path.isdir(name):  # isdir判断文件是否为文件夹
            # new_name=name.replace('jpg','gif')    # 修改后缀名
            os.rename(name, str(index) + '.jpg')    # os.rename(src,dst)重命名文件或目录，从 src 到 dst

    os.chdir(currentpath)  # 再把工作目录切回来


if __name__ == '__main__':
    filerename()
